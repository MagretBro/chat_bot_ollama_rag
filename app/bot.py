import asyncio
import httpx
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN =  "8039706333:AAEGbRSIN9ry3Jgy2SluPQe38uUErUzj2Os"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "gemma3:12b"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Напиши:\n/gemma твой вопрос"
    )


async def gemma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Напиши вопрос после /gemma")
        return

    await update.message.reply_text("🤔 Думаю...")

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            answer = response.json()["response"]

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
