# app.py – Hauptanwendung (Streamlit-Startpunkt)
import streamlit as st
from data.stock_data import StockDataManager
import plotly.graph_objs as go

# Konfiguriere die Seite
st.set_page_config(page_title="GPW Trading AI", layout="centered")

# Überschrift und ein kleiner Willkommenstext
st.title("🇵🇱 GPW Trading AI Assistant")
st.write("Willkommen zu meiner Streamlit-Web-App für die Warschauer Börse! Live_Kursanalyse für KGHM")

# Hole Daten
stock_manager = StockDataManager()
data = stock_manager.get_stock_data()

# Zeige aktuellen Kurs
current_price = data["Close"].iloc[-1]
st.metric("Aktueller Kurs (PLN)", f"{current_price:.2f}")

# Einfaches Diagramm
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Kurs"))
fig.update_layout(title="KGHM Kursentwicklung (1 Monat)", xaxis_title="Datum", yaxis_title="PLN")
st.plotly_chart(fig)