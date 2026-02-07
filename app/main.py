import requests
import os

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:12b"

def query_gemma(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.7, "max_tokens": 200}
    }
    try:
        resp = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json().get("response", "Нет ответа от модели")
    except Exception as e:
        return f"Ошибка при запросе к Gemma: {e}"

if __name__ == "__main__":
    question = "какая у тебя дата сейчас? в каком времени ты живешь?"
    answer = query_gemma(question)
    print("Gemma отвечает:\n", answer)
