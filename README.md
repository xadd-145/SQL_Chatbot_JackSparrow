# Captain Jack Sparrow: Database Treasure Hunter 🏴‍☠️⚓

---

**Captain Jack Sparrow** be no ordinary assistant — he’s a Streamlit-powered AI navigator built with **Claude-3 Opus** and **LangChain**.  
Talk in plain English, and the good Captain wrangles your database, fishes the right SQL, and serves you treasures in clean tables or lists.

No clunky dashboards.  
No ugly errors.  
Only treasure maps and gold coins (well, almost). 🏴‍☠️

---

## 🏴‍☠️ Features

- **Natural Language to SQL**: Just say "Find all ships docked at Port of Singapore" — Captain takes the wheel.
- **Schema-Aware**: No hallucinated columns, no getting lost at sea — Claude always gets the schema map.
- **Error Handling, Pirate-Style**: If trouble be brewin', you'll hear it fair and square.
- **Formatted Results**: Scrolls (markdown lists) or tables — polished treasure, not messy loot.
- **Streamlit Frontend**: Interactive, fast, cleaner than the deck of the Black Pearl.

---

## ⚓ Project Treasure Map

```
/
|-- sql_agent.py         # Main Streamlit app (Captain's brain)
|-- .env                 # Environment variables (Claude's secret map)
|-- requirements.txt     # Python dependencies (rum not included)
|-- README.md             # This very scroll
```

---

## 🧭 Setting Sail (Setup Instructions)

1. **Clone the ship repository**

```bash
git clone https://github.com/Sahil-Shimpi/sql_assistant.git
```

2. **Create yer `.env` scroll**

```bash
ANTHROPIC_API_KEY=yer_secret_claude_api_key_here
```

3. **Stock up on supplies (Install dependencies)**

```bash
pip install -r requirements.txt
```

4. **Raise the sails (Run the Streamlit app)**

```bash
streamlit run sql_agent.py
```

5. **Man the wheel (Open yer browser)**

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🗺️ How Captain Jack Navigates

- Loads the database’s treasure map (schema).
- Sends yer command and the map to Claude 3 Opus.
- Claude, that clever parrot, writes valid SQL inside triple backticks.
- Captain extracts and runs the SQL on the real database.
- The treasure (answers) are laid bare!

---

## ☠️ Known Treacheries (Current Limitations)

| Sea Hazard           | Status              | Captain’s Notes             |
| -------------------- | ------------------- | ---------------------------- |
| Table Name Guessing  | ✅ Solved            | Schema known to the Captain |
| Column Guessing      | ⚠️ Partially solved | Mind the spelling!           |
| Case Sensitivity     | ⚠️ Partially solved | Tread carefully, matey       |
| Schema Validation    | ❌ Not solved        | Trust the first mate (Claude) |
| Complex Joins        | ✅ Mostly solved     | Be explicit with orders      |
| Persistent Memory    | ❌ Not solved        | Each voyage starts fresh     |
| Raw SQL Errors       | ✅ Solved            | Warnings, not explosions     |

---

## 🛠️ Future Upgrades for the Black Pearl

- SQL Pre-Validation (before firing cannons)
- Memory Buffer (so Captain Jack remembers past voyages)
- Smarter JOIN Maps
- Advanced Treasure Categorization (Error Types)

---

## ✨ Credits

- Ship built and steered by **Sahil Shimpi** ⚓
- Powered by the magic of **Claude 3 Opus (Anthropic)**, **LangChain**, and **Streamlit** 🌊
- Inspired by a dream: **databases so simple, even pirates can query 'em.**

---

## 📜 License

This be an open source ship under the MIT License.  
Steal, fork, contribute — but always leave a good bottle of rum. 🍻

---

## 🏴‍☠️ Contributing

Got an idea to make Captain Jack smarter?  
Spot a reef he didn’t see?  
Raise yer flag, fork the repo, and open a pull request!

> "The sea may be vast, but the right question points the way to treasure."  
> — Captain Jack Sparrow

---

**Ready to chart your own database adventure?**  
**Let’s sail. 🧭🏴‍☠️**

---
