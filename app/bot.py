import asyncio
#import httpx
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from scripts.rag_ask import ask_with_rag
load_dotenv()


BOT_TOKEN =  os.getenv("BOT_TOKEN")
#OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
#MODEL = "gemma3:12b"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Напиши:\n/gemma твой вопрос"
    )


async def gemma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Напиши вопрос после /gemma")
        return

    await update.message.reply_text("🤔 Думаю...")

    try:
        answer = ask_with_rag(question)
        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")



def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gemma", gemma))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
