# Captain Jack Sparrow: Database Treasure Hunter 🏴‍☠️⚓

[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-fc466b?logo=streamlit)](https://streamlit.io/)
[![Powered by Claude 3.5 Sonnet](https://img.shields.io/badge/Powered%20by-Claude%203.5%20Sonnet-blueviolet)](https://www.anthropic.com/index/claude)
[![LangChain Integration](https://img.shields.io/badge/Integration-LangChain-00bcd4)](https://www.langchain.dev/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://github.com/Sahil-Shimpi)

---

## 📚 Table of Contents

- [Features](#-features)
- [Project Treasure Map](#-project-treasure-map)
- [Setting Sail (Setup Instructions)](#-setting-sail-setup-instructions)
- [How Captain Jack Navigates](#-how-captain-jack-navigates)
- [Known Treacheries (Current Limitations)](#-known-treacheries-current-limitations)
- [Upcoming Upgrades for the Black Pearl](#-upcoming-upgrades-for-the-black-pearl)
- [Credits](#-credits)
- [License](#-license)
- [Contributing](#-contributing)

---

**Captain Jack Sparrow** ain't no ordinary database mate.  
He’s a Streamlit-powered navigator, built with **Claude 3.5 Sonnet** and **LangChain**, ready to turn yer plain English into real SQL magic.  
Speak like a sailor or a scholar — Captain fetches yer answers from the deepest database dungeons.

No dashboards.  
No crashes.  
Just straight treasure retrieval. 📜

---

## 🏴‍☠️ Features

- **Natural Language to SQL**: Just whisper, “Show cargos in 2024,” and the Captain takes the helm.
- **Schema-Aware Navigation**: No hallucinations — only real ports and planks. Schema context stays in Claude’s compass.
- **Error Handling, Pirate-Style**: If ye strike trouble, Jack flags it clean — no cryptic scrolls.
- **Formatted Treasures**: Results show up as golden tables or polished lists.
- **Interactive UI via Streamlit**: Smooth as sailing on calm waters.

---

## ⚓ Project Treasure Map

```
/
|-- sql_agent.py         # Captain's main compass (Streamlit app)
|-- .env                 # Claude’s API key goes here (don't lose this scroll!)
|-- requirements.txt     # What ye need to sail (dependencies)
|-- README.md            # Ye be readin’ it now, mate
```

---

## 🧭 Setting Sail (Setup Instructions)

1. **Clone the Ship (Repo)**

```bash
git clone https://github.com/Sahil-Shimpi/sql_assistant.git
```

2. **Hide Yer Secret Map**

```bash
# Inside .env file
ANTHROPIC_API_KEY=your_claude_api_key_here
```

3. **Stock the Ship**

```bash
pip install -r requirements.txt
```

4. **Hoist the Colors (Launch the App)**

```bash
streamlit run sql_agent.py
```

5. **Open the Captain’s Deck**

Visit: [http://localhost:8501](http://localhost:8501)

---

## 🗺️ How Captain Jack Navigates

- Loads the database’s schema scrolls into memory.
- Sends yer question plus schema context to **Claude 3.5 Sonnet**.
- Claude conjures the right SQL inside triple backticks (savvy?).
- The code be run safely, with treasure (results) fetched and polished.
- Output is tabled or listed — no confusion, no shipwrecks.

---

## ☠️ Known Treacheries (Current Limitations)

| Stormy Waters         | Status              | Captain’s Notes               |
| --------------------- | ------------------- | ------------------------------ |
| Column Guessing       | ⚠️ Partial           | Watch yer typos, sailor        |
| Case Sensitivity      | ⚠️ Partial           | Be precise, lest ye be sunk    |
| Schema Validation     | ❌ Not yet           | Trust in Claude, aye           |
| Persistent Memory     | ❌ None              | Jack forgets each voyage       |

---

## ⚒️ Upcoming Upgrades for the Black Pearl

- SQL Dry Run (pre-execution check)
- Memory of Past Voyages (chat + schema memory)
- Join Optimization (mapping joins smarter)
- Result Formatting Upgrades (charts, summaries, and more)

---

## ✨ Credits

- Ship built and captained by **Sahil Shimpi** & **Aditi Patil** ⚓  
- Foundational code and debugging support graciously provided by **[Omniwot](https://github.com/Omniwot)** 🌟  
- Powered by the magic of **Claude 3.5 Sonnet (Anthropic)**, **LangChain**, and **Streamlit**  
- Inspired by the dream: *making databases as easy to explore as a pirate's map.*

---

## 📜 License

Licensed under the MIT License —  
Fork it, build on it, contribute back — always credit those who helped chart the course. ⚓

---

## 🏴‍☠️ Contributing

Got an idea to sharpen Captain Jack’s instincts?  
Spot a reef he didn’t see?  
Raise yer flag, fork the repo, and open a pull request!

> *“The sea may be uncertain... but with the right query, the treasure always reveals itself.”*  
> – Captain Jack Sparrow

---

**Ready to embark on your own database voyage?**  
**Let’s sail. 🧭🏴‍☠️**

---
