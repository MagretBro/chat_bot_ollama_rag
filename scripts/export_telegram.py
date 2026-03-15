from telethon import TelegramClient
from dotenv import load_dotenv
import os
import json
from pathlib import Path
from datetime import timezone
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

API_ID = int(os.getenv("TG_API_ID"))
API_HASH = os.getenv("TG_API_HASH")

# Путь к файлу состояния
STATE_FILE = Path("state/telegram_state.json")
os.makedirs(STATE_FILE.parent, exist_ok=True)

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_message_id": 0}

def save_state(last_message_id: int):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"last_message_id": last_message_id}, f, ensure_ascii=False, indent=2)

client = TelegramClient("parser_session", API_ID, API_HASH)
CHANNELS = ["analysts_hunter", "data_analysis_ml"]
LIMIT_PER_CHANNEL = 300
OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def main():
    print("Connecting to Telegram...")
    await client.start()
    print("Connected:", await client.is_user_authorized())
    state = load_state()
    last_id = state.get("last_message_id", 0)

    for channel in CHANNELS:
        messages_data = []
        async for message in client.iter_messages(channel, limit=LIMIT_PER_CHANNEL):
            if not message.text:
                continue
            messages_data.append({
                "id": message.id,
                "date": message.date.astimezone(timezone.utc).isoformat() if message.date else None,
                "text": message.text,
            })
        if messages_data:
            max_id = max(m["id"] for m in messages_data)
            save_state(max_id)
        output_path = f"{OUTPUT_DIR}/{channel}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(messages_data, f, ensure_ascii=False, indent=2)

with client:
    client.loop.run_until_complete(main())