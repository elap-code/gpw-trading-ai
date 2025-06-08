# app.py – Hauptanwendung (Streamlit-Startpunkt)
import streamlit as st
from data.stock_data import StockDataManager
import pandas as pd
import plotly.graph_objs as go
from ai.analyzer import AIAnalyzer
import ollama


# Konfiguriere die Seite
st.set_page_config(page_title="GPW Trading AI", layout="centered")

available_stocks = {
    "KGHM": "KGH.WA",
    "PKN Orlen": "PKN.WA",
    "PKO Bank": "PKO.WA",
    "CD Projekt": "CDR.WA",
    "JSW": "JSW.WA",
    "Allegro": "ALE.WA",
    "Asseco": "ACP.WA",
    "Santander Bank": "SPL.WA",
    "mBank": "MBK.WA",
    "LPP": "LPP.WA",
    "PZU": "PZU.WA"
}

# Aktienauswahl
selected_names = st.multiselect("📊 Wähle Aktien für Vergleich", list(available_stocks.keys()), default=["KGHM", "PKN Orlen"])

# Initialisiere Datenmanager und Diagramm
stock_manager = StockDataManager()
fig = go.Figure()
kursdaten = []

# Lade Daten für jede ausgewählte Aktie
for name in selected_names:
    symbol = available_stocks[name]
    df = stock_manager.get_history(symbol, period="1mo")
    current_price = stock_manager.get_current_price(symbol)
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name=name))
    kursdaten.append({"Aktie": name, "Kurs (PLN)": round(current_price, 2)})

# Zeige das Diagramm
fig.update_layout(title="📈 Kursvergleich (1 Monat)", xaxis_title="Datum", yaxis_title="PLN")
st.plotly_chart(fig)

# Zeige aktuelle Kurse
st.subheader("📍 Aktuelle Kurse")
kurs_df = pd.DataFrame(kursdaten)
st.table(kurs_df)

# KI-Analysebereich
st.subheader("🧠 KI-Analyse")
analyze = st.button("Analyse starten")

if analyze and selected_names:
    analyzer = AIAnalyzer()
    stock_to_analyze = selected_names[0]
    df = stock_manager.get_history(available_stocks[stock_to_analyze], period="1mo")
    df_string = df["Close"].to_string()
    # KI-Analyse (Englisch)
    result = analyzer.analyze_stock(stock_to_analyze, df_string)
    st.text_area("💬 KI-Ergebnis (Englisch)", result, height=250)
    # Automatisch ins Deutsche übersetzen
    translation_prompt = f"Übersetze diesen Text ins Deutsche:\n\n{result}"
    translation = ollama.chat(model="llama3", messages=[{"role": "user", "content": translation_prompt}])
    translated_text = translation["message"]["content"]

    st.text_area("💬 KI-Ergebnis (Deutsch)", translated_text, height=250)

