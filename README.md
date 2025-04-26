# Jarvis: Claude-Powered SQL Assistant 🪲

---

**Jarvis** is a lightweight, Streamlit-powered AI database assistant built using **Claude-3 Opus** and **LangChain**. It lets you query your database schema using natural language, automatically generates SQL, executes it safely, and displays results in clean tables or markdown lists.

Forget clunky BI tools. With Jarvis, your database talks back.

---

## ✨ Features

- **Natural Language to SQL**: Just type "Show all cargos in transit" — Jarvis handles the rest.
- **Schema-Aware**: No hallucinated columns or wrong tables (schema is passed into Claude every time).
- **Clean Error Handling**: Human-readable errors. No ugly SQL crashes.
- **Formatted Results**: Single values, bullet points, and full tables — automatically displayed.
- **Streamlit Frontend**: Fully interactive, clean, and expandable.

---

## 🌍 Project Structure

```
/
|-- sql_agent.py         # Main Streamlit app
|-- .env                 # Environment variables (Claude API key)
|-- requirements.txt     # Python dependencies
|-- README.md             # This file
```

---

## 🚀 Setup Instructions

1. **Clone the repository**

```
https://github.com/Sahil-Shimpi/sql_assistant.git
```

2. **Create ****`.env`**** file**

```
ANTHROPIC_API_KEY=your_claude_api_key_here
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start the Streamlit app**

```bash
streamlit run sql_agent.py
```

5. **Open your browser**

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🤖 How Jarvis Works

- Loads database schema context.
- Sends your user query and schema info to Claude 3 Opus.
- Claude generates executable SQL inside triple backticks.
- App safely extracts and runs SQL on your live database.

---

## 📉 Current Limitations

| Category            | Status              | Notes                       |
| ------------------- | ------------------- | --------------------------- |
| Table Name Guessing | ✅ Solved            | Schema context passed       |
| Column Guessing     | ⚠️ Partially solved | No hard validation          |
| Case Sensitivity    | ⚠️ Partially solved | Minor risk                  |
| Schema Validation   | ❌ Not solved        | Trusting Claude's SQL       |
| Complex Joins       | ✅ Mostly solved     | Needs explicit user queries |
| Persistent Memory   | ❌ Not solved        | Each prompt is stateless    |
| Raw SQL Errors      | ✅ Solved            | Nice error messages         |

---

## 🚧 Planned Improvements

- SQL Pre-Validation (before running queries)
- Memory Buffer to "remember" previous chats
- Intelligent JOIN suggestions
- Smarter error categorization

---

## 🌟 Credits

- Built by **Sahil Shimpi**
- Powered by **Claude 3 Opus (Anthropic)** + **LangChain** + **Streamlit**
- Inspired by the dream of making databases conversational.

---

## 🚀 License

This project is open source under the MIT License.

---

## 🚀 Contributing

If you have ideas to make Jarvis smarter or faster, feel free to fork and open a pull request!

> "A database is only as powerful as the questions you can ask it."\
> — Jarvis

---

**Ready to meet your database's new best friend?**\
**Let's go. 🚀**

