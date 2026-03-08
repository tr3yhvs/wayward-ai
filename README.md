# 🧭 Wayward AI

**Offline AI travel assistant for vanlife, RV and overlanding travelers.**  
**флайн AI-ассистент для ванлайферов, путешественников на RV и оверлендеров.**

---

## ⚠️ Disclaimer / тказ от ответственности

EN: This tool is for emergency reference only. Always verify critical information with local sources. Seek professional help when possible. The author is not responsible for decisions made based on this data.

RU: тот инструмент предназначен только для справочного использования в экстренных ситуациях. сегда проверяйте важную информацию из местных источников. ри возможности обращайтесь к профессионалам. втор не несёт ответственности за решения, принятые на основе этих данных.

---

## 🌍 What is Wayward AI? / то такое Wayward AI?

**EN:**  
Wayward AI is an offline-first travel assistant built for people who travel in remote areas with no internet connection. It works via a local LLM (Ollama) and switches to Claude API when online.

**RU:**  
Wayward AI — это офлайн-ассистент для путешественников в отдалённых районах без интернета. аботает через локальную LLM (Ollama), при наличии интернета переключается на Claude API.

---

## ✨ Features / озможности

| Feature | EN | RU |
|---|---|---|
| 🗺️ Risk Analysis | Road, weather, wildlife risks by region | иски дорог, погоды, дикой природы по регионам |
| 🔧 DIY Repair | Offline repair guides (tire, engine, solar) | флайн гайды по ремонту |
| 💧 Survival | Water, fire, shelter, navigation guides | айды по воде, огню, укрытию, навигации |
| 🌱 Green Routing | Fuel cost and CO2 calculator | асчёт топлива и CO2 |
| 🤝 Community Sync | Add spots offline, sync when connected | обавляй споты офлайн, синхронизируй при связи |
| 🌐 Multilingual | English, Spanish, Russian | нглийский, испанский, русский |

---

## 🗺️ Supported Regions / оддерживаемые регионы

- 🏔️ Caucasus (Georgia, Armenia, Turkey)
- 🐪 Central Asia (Kazakhstan, Kyrgyzstan, Tajikistan, Mongolia)
- 🌄 Latin America (Patagonia, Andes)
- 🌍 Africa (Morocco, Namibia)
- 🦘 Oceania (Australian Outback)
- 🌲 Siberia (Altai, Baikal)

---

## 🚀 Quick Start / ыстрый старт

**Requirements / Требования:**
- Python 3.10+
- [Ollama](https://ollama.com) for offline LLM
- Anthropic API key (optional, for online mode)

**Installation / Установка:**
`ash
git clone https://github.com/tr3yhvs/wayward-ai.git
cd wayward-ai
pip install streamlit faiss-cpu sentence-transformers requests ollama anthropic
ollama pull llama3.2:1b
`

**Run / апуск:**
`ash
# Web interface / еб-интерфейс
streamlit run app.py

# Terminal / Терминал
python main.py
`

**Optional: Claude API / пционально: Claude API:**
`ash
set ANTHROPIC_API_KEY=your_key_here
`

---

## 💬 Example Queries / римеры запросов
`
what are the risks in caucasus in april
my tire is flat
engine won't start
how to find water in desert
best route from Tbilisi to Yerevan
I feel lonely been alone for weeks
`

---

## 🛠️ Tech Stack / Технологии

- Python 3.14
- Ollama (llama3.2:1b) — offline LLM
- Claude API — online fallback
- Streamlit — web UI
- SQLite — risk database
- FAISS + sentence-transformers — vector search RAG
- OSM tiles — offline maps

---

## 🤝 Contributing / клад в проект

EN: Pull requests are welcome! Please review information carefully before submitting — accuracy of survival and safety data is critical.

RU: Pull request'ы приветствуются! ожалуйста, тщательно проверяйте информацию перед отправкой — точность данных о выживании и безопасности критически важна.

---

## 📄 License / ицензия

MIT License — free to use, modify and distribute.  
MIT ицензия — свободно использовать, изменять и распространять.

---

## 👤 Author / втор

Built by [@tr3yhvs](https://github.com/tr3yhvs)  
Idea born from real overlanding experience in the Caucasus region.
