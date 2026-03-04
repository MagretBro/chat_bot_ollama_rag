import json
import chromadb
from chromadb.config import Settings

DATA_FILE = "data/rag_documents_analysts_hunter.json"
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

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        docs = json.load(f)

    texts = []
    metadatas = []
    ids = []

    for i, d in enumerate(docs):
        if not d.get("text"):
            continue
        texts.append(d["text"])
        metadatas.append({
            "date": d.get("date"),
            "source": "telegram"
        })
        ids.append(str(i))

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )


    print(f"✅ Загружено документов: {len(texts)}")

if __name__ == "__main__":
    main()
