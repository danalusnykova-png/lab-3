# Документування пакета для обробки оцінок студентів

Практична робота, завдання 4. Проєкт продовжує завдання 3.
Програма перевіряє оцінки, читає текстовий файл та обробляє власні виключення.

## Структура

```text
task3_student_package/
├── README.md
├── requirements.txt
├── demo_exports.py
├── demo_docs.py
├── data/
│   └── student_grades.txt
└── student_app/
    ├── __init__.py
    ├── __main__.py
    ├── app.py
    ├── models/
    │   ├── __init__.py
    │   └── exceptions.py
    └── services/
        ├── __init__.py
        ├── grades.py
        ├── storage.py
        └── logger.py
```

## Запуск з кореня проєкту

У Windows:

```cmd
py -m student_app
py demo_docs.py
py demo_exports.py
```

Якщо команда `py` недоступна, використовуйте `python` замість `py`.

## Документування

- Стиль docstrings: **Google**, описи українською мовою.
- У функціях та методах використано секції `Args:`, `Returns:`, `Raises:`.
- Анотації типів є в сигнатурах функцій і методів.
- Приклади вбудованих параметризованих типів: `list[str]`, `dict[str, int]`.
- `demo_docs.py` показує результати `help()`, `__doc__`, `__name__`, `__annotations__`.

Сторонніх бібліотек не потрібно. Підходить Python 3.9+.
