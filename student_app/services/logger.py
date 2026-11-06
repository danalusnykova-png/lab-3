"""Модуль запису повідомлень про помилки в текстовий журнал."""

from pathlib import Path
from typing import Union


def save_error(message: str, filename: Union[str, Path]) -> None:
    """Додати повідомлення про помилку в кінець текстового файлу.

    Args:
        message (str): Текст повідомлення.
        filename (Union[str, Path]): Назва або шлях до файлу журналу.

    Returns:
        None: Функція тільки записує текст у файл.

    Raises:
        OSError: Не вдалося відкрити файл або записати в нього дані.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(message + "\n")
