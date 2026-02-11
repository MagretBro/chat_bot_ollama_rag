from telethon import TelegramClient
from dotenv import load_dotenv
import json
import os
from datetime import timezone

load_dotenv()
# ====== НАСТРОЙКИ ======
CHANNELS = [
    "analysts_hunter", 
    "data_analysis_ml",
]

LIMIT_PER_CHANNEL = 300  # ограничение на кол-во сообщений
OUTPUT_DIR = "data/raw"

# ====== КОНФИГ ИЗ ENV ======
API_ID = int(os.getenv("TG_API_ID"))
API_HASH = os.getenv("TG_API_HASH")

if not API_ID or not API_HASH:
    raise RuntimeError("TG_API_ID или TG_API_HASH не заданы")

os.makedirs(OUTPUT_DIR, exist_ok=True)

client = TelegramClient("parser_session", API_ID, API_HASH)


async def main():
    await client.start()
    print("✅ Telegram client started")

    for channel in CHANNELS:
        print(f"📥 Загружаю канал: {channel}")
        messages_data = []

        async for message in client.iter_messages(channel, limit=LIMIT_PER_CHANNEL):
            if not message.text:
                continue

            messages_data.append({
                "id": message.id,
                "date": message.date.astimezone(timezone.utc).isoformat() if message.date else None,
                "text": message.text,
                "views": message.views,
                "forwards": message.forwards,
                "replies": message.replies.replies if message.replies else 0,
            })

        output_path = f"{OUTPUT_DIR}/{channel}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(messages_data, f, ensure_ascii=False, indent=2)

        print(f"✅ Сохранено {len(messages_data)} сообщений → {output_path}")

    await client.disconnect()
    print("🏁 Готово")


with client:
    client.loop.run_until_complete(main())
