import json
from datetime import datetime

SOURCE_NAME = "analysts_hunter"

INPUT_FILE = "data/raw/analysts_hunter.json"
OUTPUT_FILE = "data/rag_documents_analysts_hunter.json"


def clean_text(text: str) -> str:
    return text.strip()


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    messages = json.load(f)

rag_docs = []

for msg in messages:
    text = msg.get("text")

    if not text:
        continue

    text = clean_text(text)

    if len(text) < 10:
        continue

    date_raw = msg.get("date")
    date = date_raw.split("T")[0] if date_raw else None

    rag_docs.append({
        "source": SOURCE_NAME,
        "date": date,
        "text": text
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(rag_docs, f, ensure_ascii=False, indent=2)

print(f"Готово. Документов для RAG: {len(rag_docs)}")
