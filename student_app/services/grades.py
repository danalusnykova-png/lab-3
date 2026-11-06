"""Перевірка оцінок і обчислення середнього бала студентів.

Модуль містить функції перевірки введення, прохідного бала та оцінок із файлу.
"""

from ..models import GradeValidationError, LowGradeError
from .logger import save_error


def parse_grade(value: str) -> int:
    """Перетворити текстову оцінку на число від 0 до 100.

    Args:
        value (str): Оцінка, введена як текст.

    Returns:
        int: Перевірена оцінка.

    Raises:
        GradeValidationError: Значення не є цілим числом або поза межами 0–100.
    """
    try:
        grade = int(value)
    except (ValueError, TypeError) as error:
        raise GradeValidationError("оцінка", value) from error

    if not 0 <= grade <= 100:
        raise GradeValidationError("оцінка", value)
    return grade


def check_passed(grade: int, minimum: int = 60) -> str:
    """Перевірити, чи студент набрав потрібний прохідний бал.

    Args:
        grade (int): Оцінка студента.
        minimum (int): Мінімальна прохідна оцінка.

    Returns:
        str: Повідомлення про успішне складання предмета.

    Raises:
        LowGradeError: Оцінка студента менша за minimum.
    """
    if grade < minimum:
        raise LowGradeError(grade, minimum)
    return "Студент склав предмет"


def check_with_log(grade: int, log_filename: str) -> str:
    """Перевірити оцінку, а помилку записати у файл і підняти знову.

    Args:
        grade (int): Оцінка студента.
        log_filename (str): Шлях до файлу журналу.

    Returns:
        str: Повідомлення, якщо предмет складено.

    Raises:
        LowGradeError: Оцінка нижча за прохідний бал.
        OSError: Не вдалося записати повідомлення у файл журналу.
    """
    try:
        return check_passed(grade)
    except LowGradeError as error:
        save_error(str(error), log_filename)
        print("Помилку записано в журнал")
        raise


def calculate_average(total: str, count: str) -> float:
    """Обчислити середню оцінку за сумою та кількістю.

    Args:
        total (str): Сума оцінок, записана текстом.
        count (str): Кількість оцінок, записана текстом.

    Returns:
        float: Середній бал студента.

    Raises:
        ValueError: Одне зі значень не можна перетворити на ціле число.
        ZeroDivisionError: Кількість оцінок дорівнює нулю.
    """
    return int(total) / int(count)


def parse_student_grades(lines: list[str]) -> dict[str, int]:
    """Зібрати оцінки студентів із рядків текстового файлу.

    Args:
        lines (list[str]): Рядки виду «Ім'я: оцінка».

    Returns:
        dict[str, int]: Словник, де ключ є ім'ям, а значення є оцінкою.

    Raises:
        ValueError: Рядок не містить роздільника або імені студента.
        GradeValidationError: Оцінка в рядку неправильна.
    """
    result: dict[str, int] = {}

    for line in lines:
        if not line.strip():
            continue

        if ":" not in line:
            raise ValueError(f"Неправильний рядок: {line}")

        student, value = line.split(":", 1)
        student = student.strip()
        if not student:
            raise ValueError("Не вказано ім'я студента")

        result[student] = parse_grade(value.strip())

    return result
