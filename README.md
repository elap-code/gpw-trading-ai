# 🇵🇱 GPW Trading AI Assistant

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gpw-trading-ai.streamlit.app)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI-powered trading assistant for Warsaw Stock Exchange (GPW) with real-time analysis, technical indicators, and intelligent predictions.**

![GPW Trading AI Preview](assets/dashboard.png)

## 🚀 Features

- 📊 Real-time GPW Stock Data – Live data via Yahoo Finance API
- 🤖 AI-Powered Analysis – Trend detection and predictions
- 📈 Interactive Charts – Candlestick charts + indicators
- ⚡ Technical Indicators – SMA, Resistance, Volatility
- 🎯 Risk Assessment – Automated risk level evaluation
- 🇵🇱 Polish Market Focus – Specialized for GPW
- 📱 Responsive Streamlit Interface

## 🏃‍♂️ Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/elap-code/gpw-trading-ai.git
cd gpw-trading-ai

python -m venv venv
venv\Scripts\activate     # Windows
# oder für Mac/Linux:
# source venv/bin/activate

pip install -r requirements.txt
streamlit run src/app.py
```

Die App öffnet sich unter `http://localhost:8501`.

## 🌐 Live Demo

🔗 **[Jetzt ausprobieren](https://gpw-trading-ai.streamlit.app)** *(nach Deployment)*

## 📊 Unterstützte Unternehmen

| Symbol    | Firma                  | Sektor               |
|-----------|------------------------|----------------------|
| PKO.WA    | PKO Bank Polski        | Banking              |
| PKN.WA    | PKN Orlen              | Energy               |
| CDR.WA    | CD Projekt             | Gaming/Tech          |
| ALE.WA    | Allegro                | E-commerce           |
| JSW.WA    | Jastrzębska Węglowa    | Mining               |
| LPP.WA    | LPP                    | Fashion/Retail       |
| CPS.WA    | Cyfrowy Polsat         | Telecommunications   |
| ZUE.WA    | ZUE S.A.               | Rail Infrastructure  |
| ZEP.WA    | ZE PAK                 | Energy               |
| TPE.WA    | Tauron Polska Energia  | Energy               |
| UNI.WA    | UNIBEP                 | Construction         |
| PUE.WA    | Pure Biologics         | Biotech              |
| PGS.WA    | Polenergia             | Green Energy         |
| NST.WA    | Nestmedic              | MedTech              |
| KGH.WA    | KGHM                   | Mining               |
| ENA.WA    | ENEA                   | Energy               |
| AST.WA    | Astarta                | Agriculture          |

## 🛠️ Tech Stack

- Python 3.9+
- Streamlit
- yfinance
- Plotly
- Pandas, NumPy

## 📁 Projektstruktur

```
gpw-trading-ai/
├── src/
│   ├── app.py
│   ├── data/stock_data.py
│   ├── ai/analyzer.py
│   └── utils/helpers.py
├── tests/
├── assets/
│   ├── dashboard.png
│   └── ai_analysis.png
├── requirements.txt
├── README.md
├── LICENSE
```

## 🔍 Beispielcode

```python
from src.data.stock_data import StockDataManager
from src.ai.analyzer import AIAnalyzer

stock_manager = StockDataManager()
ai_analyzer = AIAnalyzer()

data = stock_manager.get_stock_data("CDR.WA", "1mo")
analysis = ai_analyzer.analyze_stock("CDR.WA", data)
print(analysis['trend'])
```

## 🧪 Tests

```bash
pytest
pytest --cov=src
```

## 🚀 Deployment (z. B. Streamlit Cloud)

1. Repo forken oder kopieren
2. Auf [streamlit.io](https://streamlit.io) einloggen
3. Neues Projekt erstellen → `src/app.py` als Start-Datei

## 🤝 Beitrag leisten

1. Fork erstellen
2. Branch anlegen: `git checkout -b feature/neue-idee`
3. Commit: `git commit -m "Add neue Funktion"`
4. Push: `git push origin feature/neue-idee`
5. Pull Request erstellen

## 📞 Kontakt

- Issues: [GitHub Issues](https://github.com/elap-code/gpw-trading-ai/issues)
- Diskussionen: [GitHub Discussions](https://github.com/elap-code/gpw-trading-ai/discussions)
- Mail: deine.email@example.com

## ⚠️ Haftungsausschluss

Dieses Tool ist **nicht** als Finanzberatung gedacht. Du handelst immer auf eigenes Risiko.

---

**Made with ❤️ by elap-code for the Polish tech community 🇵🇱**

