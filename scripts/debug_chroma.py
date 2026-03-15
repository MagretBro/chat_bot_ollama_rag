# debug_chroma.py

from chromadb import Client
from chromadb.config import Settings
import random

client = Client(Settings(
    persist_directory="vectorstore",
    is_persistent=True
))

collection = client.get_collection("telegram_posts")

data = collection.get()

documents = data["documents"]
metadatas = data["metadatas"]

print("\n ДОКУМЕНТОВ В БАЗЕ:", len(documents))

sources = set()
for m in metadatas:
    sources.add(m.get("source"))

print("\n ИСТОЧНИКИ:")
for s in sources:
    print("-", 10)

print("\n 10 СЛУЧАЙНЫХ СООБЩЕНИЙ:")

samples = random.sample(documents, min(10, len(documents)))

for s in samples:
    print("\n---")
    print(s[:500])

