# AI Research Agent 2.0

A fully automated AI research assistant that collects, filters, clusters, summarizes, and formats high-quality AI-related content into professional-grade reports from multiple platforms.

---

## 🚀 Features

* Fetches content from:

  * 🔗 RSS Feeds (TechCrunch, OpenAI, DeepMind, etc.)
  * 📺 YouTube (e.g., Lex Fridman, Two Minute Papers)
  * 🐦 Twitter (via snscrape)
  * 👽 Reddit (r/MachineLearning, r/OpenAI)
  * 📚 arXiv (latest cs.AI and cs.LG papers)
* Summarizes long-form content using GPT
* Deduplicates and clusters stories by topic
* Downloads and embeds relevant images/screenshots
* Generates Markdown, HTML, and PDF reports

---

## 🧠 Requirements

* Python 3.9+
* API Keys for:

  * OpenAI (GPT)
  * YouTube Data API
  * Reddit API (client ID & secret)

---

## ⚙️ Setup

1. Clone the repo and enter the project folder

```bash
cd ai-research-agent
```

2. Run the setup script

```bash
chmod +x setup.sh
./setup.sh
```

3. Add your API keys and config values in `config.json`

```json
{
  "openai_api_key": "YOUR_KEY_HERE",
  ...
}
```

4. Run the agent

```bash
python main.py
```

---

## 📂 Output

After a successful run, you’ll get:

* `ai_research_report_<timestamp>.md`
* `ai_research_report_<timestamp>.html`
* `ai_research_report_<timestamp>.pdf`
* `media/` folder with saved images and screenshots

---

## 🧱 Architecture Overview

* `main.py`: Triggers the full pipeline
* `pipeline.py`: Orchestrates all steps
* `core/sources.py`: Collects data from external platforms
* `core/analyze.py`: GPT summarization, deduplication, clustering
* `core/enrich.py`: Adds media (images, screenshots, etc.)
* `core/report.py`: Builds reports (Markdown → HTML → PDF)

---

## 🔐 API Credentials

* [OpenAI API Key](https://platform.openai.com/account/api-keys)
* [YouTube Data API](https://console.developers.google.com/)
* [Reddit API App](https://www.reddit.com/prefs/apps)

---

## 📜 License

MIT License — use freely with attribution.

---

## 🧠 Coming Soon

* Semantic search across past reports
* Auto-tagging and topic maps
* Email/Notion delivery
* Live UI (optional)

---

## ✨ Contributing

Want to help expand source coverage, improve clustering, or add email delivery? PRs welcome!
