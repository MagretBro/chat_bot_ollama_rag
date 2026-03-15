import json
import chromadb
import os
import re
from chromadb.config import Settings

DATA_DIR = "data/raw"
VECTOR_DIR = "vectorstore"
COLLECTION_NAME = "telegram_posts"

def main():
    client = chromadb.Client(
        Settings(
            persist_directory=VECTOR_DIR,
            is_persistent=True,
            anonymized_telemetry=False,
        )
    )
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    existing = set(collection.get()["ids"])

    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            path = os.path.join(DATA_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                docs.extend(json.load(f))

    texts, metadatas, ids = [], [], []
    for d in docs:
        text = d.get("text")
        if not text or not is_useful(text):
            continue
            
        doc_id = f"{d['id']}"

        if doc_id in existing:
            continue
            
        texts.append(clean_text(text))
        metadatas.append({"date": d.get("date"), "source": "telegram"})
        ids.append(doc_id)

    if texts:
        collection.add(documents=texts, metadatas=metadatas, ids=ids)
        print(f"✅ Загружено документов: {len(texts)}")
    else:
        print("ℹ️ Новых документов нет")

def is_useful(text):
    if len(text) < 80:
        return False

    bad_words = ["😂", "🤣", ":)", ")))"]

    for w in bad_words:
        if w in text.lower():
            return False

    return True

def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

if __name__ == "__main__":
    main()