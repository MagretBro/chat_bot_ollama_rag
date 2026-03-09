import subprocess


def main():
    print("Шаг 1: экспорт Telegram сообщений...")
    subprocess.run(
        ["python", "scripts/export_telegram.py"],
        check=True
    )

    print("Шаг 2: обновление векторной базы...")
    subprocess.run(
        ["python", "scripts/build_vectorstore.py"],
        check=True
    )

    print("Knowledge base успешно обновлена")


if __name__ == "__main__":
    main()