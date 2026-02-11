
# Telegram RAG Bot (Gemma + Ollama)

![Telegram](https://img.shields.io/badge/Platform-Telegram-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

## Описание проекта
Это **локальный Telegram-бот**, который использует **RAG (Retrieval-Augmented Generation)** с моделью **Gemma3:12b** через **Ollama** для ответов на вопросы по контексту.  

Проект позволяет:
- Получать ответы на вопросы, учитывая контекст из заранее выгруженных данных (JSON с сообщениями из Telegram-каналов).  
- Работать полностью **локально** (без отправки данных в облако).  
- Быстро тестировать идеи с RAG и интегрировать в Telegram.  

---

## Основные возможности
- Подключение локальной модели **Gemma3:12b** через Ollama.
- Чтение контекста из JSON-файлов (`data/rag_documents_*.json`).
- Короткие и конкретные ответы 2–3 предложения.
- Локальная проверка через терминал или Telegram.
- Возможность легко добавлять новые источники данных (Telegram, CSV, JSON).

---

## Структура проекта

```text
telegram-rag-bot/
├── .venv/                # Виртуальное окружение Python
├── app/
│   ├── bot.py            # Основной код Telegram-бота
│   └── config.py         # Настройки (например, токен)
├── data/
│   └── rag_documents_*.json # Контекст для RAG
├── scripts/
│   ├── export_telegram.py # Скрипт выгрузки данных из Telegram
│   └── rag_ask.py         # Локальная RAG-функция
├── .gitignore
├── requirements.txt
└── README.md
````

---

## Установка и запуск

1. Клонируем репозиторий:

```bash
git clone https://github.com/MagretBro/chat_bot_ollama_rag.git
cd chat_bot_ollama_rag
```

2. Создаём виртуальное окружение и активируем:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

3. Устанавливаем зависимости:

```bash
pip install -r requirements.txt
```

4. Настраиваем `.env`:

```env
BOT_TOKEN=ваш_токен_бота_от_Telegram
```

5. Запускаем локальный сервер Ollama:

```bash
ollama serve
```

6. Запускаем Telegram-бот:

```bash
python app/bot.py
```

7. В Telegram:

```
/start        # Приветственное сообщение
/gemma <вопрос>  # Задать вопрос
```

---

## Пример взаимодействия

**Вопрос:**
`/gemma когда пропал "увольняка"?`

**Ответ бота:**

> Судя по тексту, увольняка пропал вчера. Контекст указывает на грусть по поводу его исчезновения. Вероятно, это повлияло на решение о поиске внешней причины для увольнения.

---

## Технологии

* **Python 3.11**
* **Telegram Bot API** (`python-telegram-bot==20.6`)
* **Ollama** (локальная модель Gemma3:12b)
* **JSON** для хранения контекста
* **RAG (Retrieval-Augmented Generation)**

---

## Планы / улучшения

* Добавить фильтры для сообщений: дата, канал, ключевые слова.
* Автоматическая очистка текста: эмодзи, ссылки, пустые сообщения.
* Метрики активности каналов: частота публикаций, популярные темы.
* Возможность подключать новые модели Ollama.

---

## Контакты

Автор: **MagretBro**
GitHub: [https://github.com/MagretBro](https://github.com/MagretBro)
