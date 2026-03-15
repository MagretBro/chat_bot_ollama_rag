from telethon import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")

client = TelegramClient("test_session", api_id, api_hash)

async def main():
    print("Connecting...")
    await client.connect()
    print("Connected:", await client.is_user_authorized())

with client:
    client.loop.run_until_complete(main())