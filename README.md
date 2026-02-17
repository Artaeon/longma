<h1 align="center">
  龙码 LóngMǎ
</h1>

<p align="center">
  <strong>Dragon Code — Learn Chinese from your terminal 🐉</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/words-119-orange?style=flat-square" alt="119 Words">
  <img src="https://img.shields.io/badge/HSK_1--5-supported-green?style=flat-square" alt="HSK 1-5">
  <img src="https://img.shields.io/badge/🇩🇪_🇬🇧-DE_%2B_EN-cyan?style=flat-square" alt="German + English">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square" alt="MIT License">
</p>

<p align="center">
  A beautiful terminal-based Mandarin Chinese learning tool,<br>
  designed for <strong>German/Austrian</strong> tech professionals with English C1.
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 **Learn** | Browse 119 tech-focused vocabulary words with Hanzi, Pinyin, and translations |
| 🃏 **Flashcards** | Study with interactive cards powered by spaced repetition (SM-2) |
| 📝 **Quiz** | Multiple choice tests to challenge your knowledge |
| 🔄 **Review** | Smart review sessions — only cards due for review appear |
| 🔊 **Pronunciation** | Full Pinyin guide with German/Austrian/English approximations |
| 📈 **Stats** | Track your streak, accuracy, mastery levels, and category progress |
| 🔍 **Search** | Find any word by Hanzi, Pinyin, German, or English |
| 🇩🇪🇬🇧 **Dual Language** | Toggle between Deutsch, English, or both |
| 💪 **Language Advantages** | Tips on how your German/Austrian dialect helps with Chinese |
| 🌐 **Offline** | Fully offline — no API calls, no internet required |

---

## 📸 Screenshots

### Welcome Screen & Main Menu
<p align="center">
  <img src="screenshots/welcome.svg" alt="Welcome screen showing the main menu with all learning modes" width="700">
</p>

### 📖 Learn Mode — Browse Tech Vocabulary
<p align="center">
  <img src="screenshots/learn_mode.svg" alt="Vocabulary browser showing tech words with Hanzi, Pinyin, German and English translations" width="700">
</p>

### 🃏 Flashcard Mode — Study with Pronunciation Hints
<p align="center">
  <img src="screenshots/flashcard.svg" alt="Flashcard reveal showing Chinese word with pronunciation guide in German" width="600">
</p>

### 🔊 Pronunciation Guide — Tones & Word Breakdown
<p align="center">
  <img src="screenshots/pronunciation.svg" alt="Pronunciation guide showing the four tones and detailed word breakdown" width="700">
</p>

### 💪 Your Language Advantages
<p align="center">
  <img src="screenshots/advantages.svg" alt="Language advantage tips showing how German and Austrian dialect help learn Chinese" width="600">
</p>

### 📈 Progress Statistics
<p align="center">
  <img src="screenshots/stats.svg" alt="Progress statistics showing streak, accuracy, mastery levels and review status" width="500">
</p>

---

## 🚀 Installation

```bash
git clone https://github.com/Artaeon/longma.git
cd longma

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install
pip install -e .
```

## 📦 Usage

```bash
# Run the CLI
chinese-cli

# Or via Python module
python -m chinese_cli
```

---

## 📚 Vocabulary Categories

| Category | Words | Focus |
|----------|-------|-------|
| 📚 **Basics** | 30 | Greetings, numbers, pronouns, essential verbs |
| 💻 **Tech** | 39 | Software, hardware, AI/ML, coding, DevOps |
| 💼 **Business** | 25 | Meetings, contracts, startups, negotiations |
| 🍜 **Daily** | 25 | Food, transport, weather, small talk |

All vocabulary entries include:
- **汉字** (Hanzi) — Chinese characters
- **拼音** (Pinyin) — Romanized pronunciation with tone marks
- **🇩🇪 Deutsch** — German translation
- **🇬🇧 English** — English translation
- **HSK Level** — Official proficiency level (1-5)
- **Example sentence** — In Chinese, Pinyin, German, and English

---

## 🔊 Pronunciation System

LóngMǎ includes a comprehensive pronunciation guide that maps every Pinyin sound to approximations in languages you already know:

### Your Superpowers 🏆

| Your Language | Chinese Sound | Why It Helps |
|---------------|---------------|--------------|
| 🇩🇪 German `ü` | Chinese `ü` | Identical! (über = nǚ) |
| 🇩🇪 German `ich`-ch | Chinese `x` | Same palatal fricative! |
| 🇩🇪 German `z` | Chinese `z` | Same [ts] sound! |
| 🇦🇹 Mühlviertlerisch | Chinese `zh/ch/sh` | Guttural sounds help with retroflexes |
| 🇷🇺 Russian `ж/ш` | Chinese `zh/sh` | Similar retroflex concept |
| 🇩🇪 German `ei/au` | Chinese `ai/ao` | Nearly identical diphthongs |

---

## 🧠 Spaced Repetition (SM-2)

LóngMǎ uses the **SM-2 algorithm** for optimal memorization:

```
Rate each card 0-5:
  0 = Complete blackout 🔴
  1 = Wrong, recognized after 🟠
  2 = Wrong, felt familiar 🟡
  3 = Correct, difficult 🟢
  4 = Correct, some hesitation 🔵
  5 = Perfect recall ⭐
```

The algorithm adjusts review intervals based on your performance — cards you struggle with appear more often, while mastered cards space out to days or weeks.

Progress is saved to `~/.chinese-cli/progress.json`.

---

## 🏗️ Architecture

```mermaid
graph TD
    A[cli.py — Main Menu] --> B[modes.py — Learn]
    A --> C[modes.py — Flashcards]
    A --> D[modes.py — Quiz]
    A --> E[modes.py — Review]
    A --> F[stats.py — Progress]
    A --> G[pronunciation.py — Guides]
    B --> H[vocab_data.py — 119 Words]
    C --> H
    D --> H
    E --> H
    C --> I[srs.py — SM-2 Engine]
    E --> I
    G --> H
    I --> J["~/.chinese-cli/progress.json"]
    
    style A fill:#0d1117,stroke:#58a6ff,color:#c9d1d9
    style H fill:#0d1117,stroke:#f0883e,color:#c9d1d9
    style I fill:#0d1117,stroke:#3fb950,color:#c9d1d9
    style G fill:#0d1117,stroke:#d2a8ff,color:#c9d1d9
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [**Rich**](https://github.com/Textualize/rich) — Beautiful terminal formatting
- [**Questionary**](https://github.com/tmbo/questionary) — Interactive prompts with arrow-key navigation
- **SM-2 Algorithm** — Spaced repetition for optimal memorization
- **JSON** — Local progress persistence (no external database)

---

## 🤝 Contributing

Contributions welcome! Ideas for improvement:
- More vocabulary categories (science, finance, travel)
- Audio playback via TTS
- HSK test simulation mode
- Import/export flashcard decks
- Multi-user support

---

## 📄 License

MIT © [Artaeon](https://github.com/Artaeon)

---

<p align="center">
  <strong>学中文，走向世界</strong><br>
  <em>Learn Chinese, reach the world</em> 🌏
</p>
