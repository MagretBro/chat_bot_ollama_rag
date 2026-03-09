import json
import subprocess
from chromadb import Client
from chromadb.config import Settings

VECTOR_DIR = "vectorstore"
COLLECTION_NAME = "telegram_posts"

# подключаем ChromaDB
client = Client(Settings(persist_directory=VECTOR_DIR, is_persistent=True, anonymized_telemetry=False))
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def search_docs(query, k=3):
    """Ищем похожие документы в ChromaDB"""
    results = collection.query(query_texts=[query], n_results=k)
    docs = results['documents'][0]
    return docs

def ask_ollama(prompt, model="gemma3:12b"):
    """Отправляем промпт в Ollama локально"""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

def ask_with_rag(question):
    # получаем k похожих документов
    docs = search_docs(question)
    context = "\n".join(f"- {d}" for d in docs)

    prompt = f"""
Ты аналитик рынка труда. Отвечай кратко, 2-3 предложения.

КОНТЕКСТ:
{context}

ВОПРОС:
{question}

Ответь кратко и по делу.
"""
    answer = ask_ollama(prompt)
    return answer

if __name__ == "__main__":
    while True:
        query = input("Вопрос: ")
        if query.lower() in ("exit", "quit"):
            break
        answer = ask_with_rag(query)
        print("\nОтвет:", answer, "\n")