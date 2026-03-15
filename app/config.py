import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Telegram API
TG_API_ID = int(os.getenv("TG_API_ID", 0))      
TG_API_HASH = os.getenv("TG_API_HASH", "")       
