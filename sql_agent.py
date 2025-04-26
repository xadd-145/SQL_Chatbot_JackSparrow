import os
import re
import pandas as pd
import streamlit as st
from decimal import Decimal
import datetime 
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.utilities import SQLDatabase

st.set_page_config(page_title="Jarvis: Claude SQL Assistant", page_icon="🤖")

# =============== ENVIRONMENT & MODEL SETUP ===============
load_dotenv()

llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    temperature=0,
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

database_uris = {
    "ddp_project_schema": "mysql+pymysql://root:S%40hil5701@localhost:3306/ddp_project_schema"
}

def set_database(db_name="ddp_project_schema"):
    if db_name in database_uris:
        uri = database_uris[db_name]
        st.session_state["db"] = SQLDatabase.from_uri(uri)
        st.session_state["current_db_name"] = db_name
    else:
        st.error(f"Database '{db_name}' not found.")

if "db" not in st.session_state:
    set_database()

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"role": "AI", "content": "Hi, I'm Jarvis, your database assistant powered by Claude. How can I help you?"}
    ]

if "schema_context" not in st.session_state:
    schema_info = []
    table_names = st.session_state["db"].get_usable_table_names()
    for table in table_names:
        try:
            columns = st.session_state["db"].get_table_info([table])
            schema_info.append(f"Table '{table}': {columns}")
        except Exception as e:
            st.warning(f"Could not fetch schema for {table}: {e}")
    st.session_state["schema_context"] = "\n".join(schema_info)

# =============== HELPER FUNCTIONS ===============

def fetch_table_schemas():
    schemas = {}
    db = st.session_state["db"]
    table_names = db.get_usable_table_names()
    for table in table_names:
        schemas[table] = db.get_table_info([table])
    return schemas

def extract_python_code(text):
    pattern = r"``````"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

def build_prompt(user_query):
    return f"""You are a Python coding assistant helping interact with a MySQL database using a SQLDatabase object called `db`.

User Question:
{user_query}

Instructions:
- FIRST, when checking a table schema, always call: 
    db.get_table_info('TableName') 
  with the table name as a **quoted string** inside single or double quotes.
- Use ONLY columns that are actually present (do NOT invent).
- If needed column like 'TransportDate' is missing, politely respond: "TransportDate column not found in the Cargo table."
- Always write: result = db.run("your_query_here")
- Always store the query output inside a variable named `result`
- Assume db.run() returns a list of tuples (NOT dictionaries).
- Access aggregates like AVG(), COUNT() using result[0][0].
- Always format numbers to 2 decimal points if displaying.
- Return ONLY executable Python code inside triple backticks ```
- Do NOT explain anything.
- Do NOT add comments.
"""

def format_result(result):
    def clean_value(val):
        if isinstance(val, Decimal):
            return float(val)
        if isinstance(val, datetime.datetime):
            return val.strftime("%Y-%m-%d %H:%M")
        return val

    if isinstance(result, list) and result:
        if all(isinstance(row, tuple) for row in result):
            if len(result) == 1:
                values = [clean_value(row) for row in result]
                if len(values) == 1:
                    v = values
                    if isinstance(v, (int, float)):
                        return f"**{v:,.2f}**"
                    return f"-  {v}"
                return "\n".join(f"-  {v}" for v in values)
            else:
                df = pd.DataFrame(result)
                df.columns = [f"Column {i+1}" for i in range(len(df.columns))]
                for col in df.columns:
                    df[col] = df[col].apply(clean_value)
                return df
        else:
            return str(result)
    if isinstance(result, Decimal):
        return f"**{float(result):,.2f}**"
    if isinstance(result, datetime.datetime):
        return result.strftime("%Y-%m-%d %H:%M")
    if isinstance(result, (int, float)):
        return f"**{result:,.2f}**"
    if isinstance(result, str):
        try:
            num = float(result)
            return f"**{num:,.2f}**"
        except ValueError:
            return result
    if isinstance(result, dict):
        return pd.DataFrame([result])
    return str(result)

def run_python_code(code_string):
    try:
        local_vars = {"db": st.session_state["db"]}
        exec(code_string, {}, local_vars)
        result = local_vars.get("result")
        if result is None:
            return "⚠️ No 'result' returned."
        return result
    except Exception as e:
        return f"⚠️ Execution Error: {str(e)}"

def handle_query(user_query):
    schema_text = st.session_state["schema_context"]
    prompt = f"""You are a Python coding assistant working with a MySQL database.

Here are the available table schemas:

{schema_text}

User Request:
{user_query}

Instructions:
- Only use tables and columns that actually exist in the schemas.
- Always query using: result = db.run("SQL Query")
- Assume db.run() returns a list of tuples (NOT dictionaries).
- NEVER print or format anything yourself.
- NEVER create extra variables like 'value'.
- Just run the query and store the output inside 'result'.
- Output ONLY the executable Python code inside triple backticks ```python.
- Do NOT explain anything.
- Do NOT add comments.
"""
    code_response = llm.invoke(prompt)
    code_to_run = extract_python_code(code_response.content)
    if not code_to_run:
        return "⚠️ No valid code generated."
    return run_python_code(code_to_run)

# =============== STREAMLIT UI ===============

st.title("Jarvis: Claude-Powered SQL Assistant")

if st.checkbox("See Connected Database Info"):
    st.success(f"Connected to: {st.session_state['current_db_name']}")

for message in st.session_state["chat_history"]:
    role = "AI" if message["role"] == "AI" else "Human"
    with st.chat_message(role):
        st.write(message["content"])

user_query = st.chat_input("Ask me something about your database...")

if user_query:
    st.session_state["chat_history"].append({"role": "Human", "content": user_query})
    with st.chat_message("Human"):
        st.write(user_query)
    with st.chat_message("AI"):
        response = handle_query(user_query)
        formatted = format_result(response)
        if isinstance(formatted, pd.DataFrame):
            st.dataframe(formatted, use_container_width=True)
        elif isinstance(formatted, str):
            st.markdown(formatted, unsafe_allow_html=True)
        else:
            st.write(formatted)
    st.session_state["chat_history"].append({"role": "AI", "content": str(response)})