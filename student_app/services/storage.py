"""Модуль читання текстових файлів з оцінками студентів."""

from pathlib import Path
from typing import Union
from ..models import StudentFileError


def read_grades(filename: Union[str, Path]) -> str:
    """Прочитати вміст файлу з оцінками студентів.

    Args:
        filename (Union[str, Path]): Шлях до текстового файлу.

    Returns:
        str: Повний вміст файлу як текст.

    Raises:
        StudentFileError: Файл не знайдено.
        OSError: Інша помилка доступу до файлу.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as error:
        raise StudentFileError(str(filename)) from error
