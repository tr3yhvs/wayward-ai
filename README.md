# 🧭 Wayward AI

**Offline AI travel assistant for vanlife, RV and overlanding travelers.**  
**Оффлайн AI-ассистент для ванлайферов, путешественников на RV и оверлендеров.**

---

## ⚠️ Disclaimer / Отказ от ответственности

**EN:**  
This tool is for emergency reference only. Always verify critical information with local sources. Seek professional help when possible. The author is not responsible for decisions made based on this data.

**RU:**  
Этот инструмент предназначен только для справочного использования в экстренных ситуациях. Всегда проверяйте важную информацию из местных источников. При возможности обращайтесь к профессионалам. Автор не несёт ответственности за решения, принятые на основе этих данных.

---

## 🌍 What is Wayward AI? / Что такое Wayward AI?

**EN:**  
Wayward AI is an offline-first travel assistant built for people who travel in remote areas with no internet connection. It works via a local LLM (Ollama) and switches to Claude API when online.

**RU:**  
Wayward AI — это оффлайн-ассистент для путешественников в отдалённых районах без интернета. Работает через локальную LLM (Ollama), при наличии интернета переключается на Claude API.

---

## ✨ Features / Возможности

| Feature          | EN                                      | RU                                           |
|------------------|-----------------------------------------|----------------------------------------------|
| 🗺️ Risk Analysis | Road, weather, wildlife risks by region | Риски дорог, погоды, дикой природы по регионам |
| 🔧 DIY Repair    | Offline repair guides (tire, engine, solar) | Оффлайн-гайды по ремонту (колесо, двигатель, солнечные панели) |
| 💧 Survival      | Water, fire, shelter, navigation guides | Гайды по воде, огню, укрытию, навигации      |
| 🌱 Green Routing | Fuel cost and CO₂ calculator            | Расчёт топлива и CO₂                         |
| 🤝 Community Sync| Add spots offline, sync when connected  | Добавляй споты оффлайн, синхронизируй при связи |
| 🌐 Multilingual  | English, Spanish, Russian               | Английский, испанский, русский               |

---

## 🗺️ Supported Regions / Поддерживаемые регионы

- 🏔️ **Caucasus** (Georgia, Armenia, Turkey)  
- 🐪 **Central Asia** (Kazakhstan, Kyrgyzstan, Tajikistan, Mongolia)  
- 🌄 **Latin America** (Patagonia, Andes)  
- 🌍 **Africa** (Morocco, Namibia)  
- 🦘 **Oceania** (Australian Outback)  
- 🌲 **Siberia** (Altai, Baikal)

---

## 🚀 Quick Start / Быстрый старт

**Requirements / Требования:**
- Python 3.10+
- [Ollama](https://ollama.com) (для оффлайн-режима)
- Anthropic API key (опционально, для онлайн-режима)

**Installation / Установка:**

```bash
git clone https://github.com/tr3yhvs/wayward-ai.git
cd wayward-ai
pip install streamlit faiss-cpu sentence-transformers requests ollama anthropic
ollama pull llama3.2:1b

Example Queries / Примеры запросовwhat are the risks in caucasus in april
my tire is flat
engine won't start
how to find water in desert
best route from Tbilisi to Yerevan
I feel lonely been alone for weeks

Tech Stack / ТехнологииPython 3.10+
Ollama (llama3.2:1b) — оффлайн LLM
Claude API — онлайн-запасной вариант
Streamlit — веб-интерфейс
SQLite — база рисков
FAISS + sentence-transformers — векторный поиск (RAG)
OSM tiles — оффлайн-карты

 Contributing / Вклад в проектPull requests приветствуются!
Пожалуйста, тщательно проверяйте всю информацию перед отправкой — точность данных о выживании и безопасности критически важна.

MIT License — свободно использовать, изменять и распространять.


Built by @tr3yhvs

