import json
import subprocess

DATA_FILE = "data/rag_documents_analysts_hunter.json"
MODEL = "gemma3:12b"
MAX_DOCS = 5  # ограничиваем контекст


def load_documents():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_context(docs):
    texts = []
    for d in docs[:MAX_DOCS]:
        texts.append(f"- {d['text']}")
    return "\n".join(texts)


def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

# ✅ ОСНОВНАЯ RAG-ФУНКЦИЯ (её будет вызывать Telegram-бот)
def ask_with_rag(question: str) -> str:
    docs = load_documents()
    context = build_context(docs)

    prompt = f"""
Ты аналитик рынка труда. Отвечай кратко, 2-3 предложения.

КОНТЕКСТ:
{context}

ВОПРОС:
{question}

Ответь кратко и по делу.
"""
    answer = ask_ollama(prompt)
    return answer[:3500]


# ✅ локальный тест из терминала
if __name__ == "__main__":
    question = input("Вопрос: ")
    answer = ask_with_rag(question)
    print("\nОТВЕТ:\n")
    print(answer)