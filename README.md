# Telegram RAG Bot (Gemma + Ollama + ChromaDB)

![Telegram](https://img.shields.io/badge/Platform-Telegram-blue)
![Python](https://img.shields.io/badge/Python-3.12-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

## Описание проекта

Это **локальный Telegram-бот**, использующий **RAG (Retrieval-Augmented Generation)** для поиска информации в сообщениях Telegram-каналов.

Бот:

1️⃣ выгружает сообщения из Telegram
2️⃣ сохраняет их в JSON
3️⃣ индексирует сообщения в **векторной базе ChromaDB**
4️⃣ выполняет **semantic search**
5️⃣ передаёт найденный контекст в **Gemma3:12b (Ollama)**
6️⃣ возвращает ответ пользователю

Все вычисления выполняются **локально**.

---

# Архитектура

```
Telegram channels
        ↓
export_telegram.py
        ↓
JSON (data/raw)
        ↓
build_vectorstore.py
        ↓
ChromaDB (vectorstore)
        ↓
semantic search
        ↓
Gemma3:12b (Ollama)
        ↓
Telegram bot answer
```

---

# Возможности

* работа **полностью локально**
* поиск по Telegram-каналам
* **vector search (semantic search)**
* интеграция с Telegram-ботом
* использование **Gemma3:12b через Ollama**
* возможность добавлять новые источники данных

---

# Структура проекта

```
telegram-rag-bot/

app/
   bot.py                 # Telegram бот
   config.py              # настройки

scripts/
   export_telegram.py     # выгрузка сообщений из Telegram
   build_vectorstore.py   # создание векторной базы
   rag_ask.py             # локальный RAG запрос
   debug_chroma.py        # диагностика базы

data/
   raw/
      *.json              # выгруженные сообщения

vectorstore/
   chroma.sqlite3         # база ChromaDB

requirements.txt
README.md
```

---

# Установка

## 1. Клонировать проект

```bash
git clone https://github.com/MagretBro/chat_bot_ollama_rag.git
cd chat_bot_ollama_rag
```

---

## 2. Создать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

---

## 3. Установить зависимости

```
pip install -r requirements.txt
```

---

# Запуск Ollama

Установить Ollama:

```
https://ollama.com
```

Запустить:

```
ollama serve
```

Скачать модель:

```
ollama pull gemma3:12b
```

---

# Индексация данных

После выгрузки сообщений из Telegram нужно построить векторную базу:

```
python scripts/build_vectorstore.py
```

---

# Проверка RAG в терминале

```
python scripts/rag_ask.py
```

Пример:

```
Вопрос:
кто ищет системного аналитика
```

---

# Запуск Telegram бота

```
python -m app.bot
```

или

```
python app/bot.py
```

---

# Диагностика базы

Посмотреть статистику базы:

```
python scripts/debug_chroma.py
```

Вывод:

```
📊 документов в базе
📡 источники
🎲 случайные сообщения
```

---

# Технологии

* Python 3.12
* Ollama
* Gemma3:12b
* ChromaDB
* python-telegram-bot
* RAG (Retrieval-Augmented Generation)

---

# Возможные улучшения

* chunking сообщений
* reranking результатов поиска
* поддержка нескольких Telegram-каналов
* автоматическое обновление базы
* web-интерфейс

---
## Контакты

Автор: **MagretBro**
GitHub: [https://github.com/MagretBro](https://github.com/MagretBro)
