# analyzer.py – Künstliche Intelligenz / Analysefunktionen
import ollama

class AIAnalyzer:
    def analyze_stock(self, stock_name: str, price_data: str):
        prompt = f"Analysiere die Aktie {stock_name}. Die Kursdaten der letzten 30 Tage:\n{price_data}\nWas fällt dir auf?"
        response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
