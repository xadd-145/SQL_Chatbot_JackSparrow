# ============================================================
# Captain Jack Sparrow: Database Treasure Hunter
# ------------------------------------------------------------
# A Streamlit application to interact with a MySQL database 
# through natural language queries, powered by Claude 3.5 (Sonnet).
# Themed after the legendary pirate, Captain Jack Sparrow!
# ============================================================

import os
import re
import pandas as pd
import streamlit as st
from decimal import Decimal
import datetime
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.utilities import SQLDatabase
import ast

# =============== STREAMLIT PAGE CONFIG ===============
st.set_page_config(page_title="Captain Jack Sparrow: Database Treasure Hunter", page_icon="🏴‍☠️")

# =============== ENVIRONMENT SETUP ===============
load_dotenv()

# Initialize Claude model
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0,
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Database connection URIs
database_uris = {
    "ddp_project_schema": "mysql+pymysql://root:S%40hil5701@localhost:3306/ddp_project_schema"
}

# Establish the database connection and store it in session state
def set_database(db_name="ddp_project_schema"):
    if db_name in database_uris:
        uri = database_uris[db_name]
        st.session_state["db"] = SQLDatabase.from_uri(uri)
        st.session_state["current_db_name"] = db_name
    else:
        st.error(f"Database '{db_name}' not found.")

if "db" not in st.session_state:
    set_database()

# Initialize conversation history with pirate flair
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"role": "AI", "content": "Ahoy! Captain Jack Sparrow here. What database treasures be ye seekin' today? 🏴‍☠️⚓️"}
    ]

# Capture and store table schema context
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

# Extract executable Python code from Claude's response
def extract_python_code(text):
    pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()

# Format query results for treasure-worthy display
def format_result(result):
    
    def clean_decimal_string(s):
        return re.sub(r"Decimal\('([\d\.]+)'\)", r"\1", s)

    def clean_value(val):
        if isinstance(val, Decimal):
            return float(val)
        if isinstance(val, datetime.datetime):
            return val.strftime("%Y-%m-%d %H:%M")
        return val

    if isinstance(result, str):
        result = clean_decimal_string(result)
        try:
            parsed = ast.literal_eval(result)
            if isinstance(parsed, (list, tuple, dict)):
                result = parsed
        except (ValueError, SyntaxError):
            st.error("❌ Failed to parse even after Decimal fix.")
            pass

    if isinstance(result, list):
        if all(isinstance(row, tuple) for row in result):
            if all(len(row) == 1 for row in result):
                return "\n".join(f"- {clean_value(row[0])}" for row in result)
            else:
                df = pd.DataFrame(result)
                df.columns = [f"Column {i+1}" for i in range(len(df.columns))]
                for col in df.columns:
                    df[col] = df[col].apply(clean_value)
                return df
        else:
            return "\n".join(f"- {clean_value(row)}" for row in result)

    elif isinstance(result, tuple):
        return "\n".join(f"- {clean_value(val)}" for val in result)

    elif isinstance(result, dict):
        return pd.DataFrame([result])

    elif isinstance(result, (Decimal, int, float)):
        return f"**{float(result):,.2f}**"

    elif isinstance(result, datetime.datetime):
        return result.strftime("%Y-%m-%d %H:%M")

    elif isinstance(result, str):
        numeric_match = re.search(r"[-+]?\d*\.\d+|\d+", result)
        if numeric_match:
            try:
                num = float(numeric_match.group())
                return f"**{num:,.2f}**"
            except Exception:
                return result
        return result

    return str(result)

# Dynamically execute Claude's generated Python code safely
def run_python_code(code_string):
    try:
        # Minor patch to auto-close missing quotes manually if needed
        if code_string.count('"') % 2 != 0 or code_string.count("'") % 2 != 0:
            code_string += '"'
        local_vars = {"db": st.session_state["db"]}
        exec(code_string, {}, local_vars)
        result = local_vars.get("result")
        return result if result is not None else "⚠️ No 'result' returned."
    except SyntaxError as e:
        return f"⚠️ SQL Syntax Error: {str(e)}"
    except Exception as e:
        return f"⚠️ Execution Error: {str(e)}"

# Build the Claude prompt and navigate the user's request
def handle_query(user_query):
    schema_text = st.session_state["schema_context"]
    prompt = f"""You are a Python coding assistant helping a pirate captain (Captain Jack Sparrow) explore a MySQL database treasure map.

Available table schemas:
{schema_text}

Captain's Request:
{user_query}

Important:
- Always wrap string values in single quotes (e.g., WHERE PortName = 'Singapore').
- Use ONLY existing tables and columns.
- Query format: result = db.run("SQL Query")
- Assume db.run() returns list of tuples.
- Output ONLY the executable Python code inside ```python ... ``` block.
- NO explanations. NO comments. Stay swift like the Black Pearl!
"""
    code_response = llm.invoke(prompt)
    code_to_run = extract_python_code(code_response.content)
    return run_python_code(code_to_run) if code_to_run else "⚠️ No valid code generated, savvy?"

# =============== STREAMLIT USER INTERFACE ===============

# Application Title
st.title("Captain Jack Sparrow: Database Treasure Hunter")

# Show connected database information if needed
if st.checkbox("See Connected Treasure (Database Info)"):
    st.success(f"Connected to: {st.session_state['current_db_name']}")

# Display chat history
for message in st.session_state["chat_history"]:
    role = "AI" if message["role"] == "AI" else "Human"
    with st.chat_message(role):
        st.write(message["content"])

# Accept new user queries
user_query = st.chat_input("What's yer next command, Captain? 🧭")

if user_query:
    st.session_state["chat_history"].append({"role": "Human", "content": user_query})
    
    with st.chat_message("Human"):
        st.write(user_query)
    
    with st.chat_message("AI"):
        response = handle_query(user_query)
        formatted = format_result(response)
        
        if isinstance(formatted, pd.DataFrame):
            st.dataframe(formatted, use_container_width=True)
        else:
            st.markdown(formatted, unsafe_allow_html=True)
    
    st.session_state["chat_history"].append({"role": "AI", "content": formatted})
