"""Головний модуль демонстрації роботи пакета з оцінками студентів."""

from pathlib import Path

# Абсолютний імпорт цілого модуля
import student_app.services.grades

# Вибірковий імпорт класів
from student_app.models import (
    StudentAppError,
    GradeValidationError,
    StudentFileError,
    LowGradeError,
)

# Відносний імпорт модуля
from .services import storage


def main() -> None:
    """Показати перевірку оцінок, читання файлу та обробку помилок.

    Args:
        Немає: Функція не приймає параметрів.

    Returns:
        None: Результати показуються в консолі.

    Raises:
        OSError: Може виникнути помилка запису журналу.
        ValueError: Можлива помилка неправильних рядків файлу з оцінками.
        GradeValidationError: Можлива неправильна оцінка в текстовому файлі.
    """
    project_folder = Path(__file__).resolve().parent.parent
    grades_file = project_folder / "data" / "student_grades.txt"
    missing_file = project_folder / "data" / "missing_grades.txt"
    log_file = project_folder / "data" / "student_errors.log"

    print("=== 1. Перевірка оцінок ===")
    print("Правильна оцінка:", student_app.services.grades.parse_grade("88"))

    try:
        student_app.services.grades.parse_grade("невідомо")
    except GradeValidationError as error:
        print("GradeValidationError:", error)

    try:
        student_app.services.grades.parse_grade("120")
    except StudentAppError as error:
        print("Перехоплено через StudentAppError:", error)

    print("\n=== 2. Читання файлу ===")
    for filename in (grades_file, missing_file):
        try:
            data = storage.read_grades(filename)
        except StudentFileError as error:
            print("StudentFileError:", error)
            print("Початкова причина через __cause__:", type(error.__cause__).__name__)
        else:
            print("Файл прочитано успішно:")
            print(data.strip())

            # Приклад роботи з параметризованими типами list[str] і dict[str, int].
            student_grades = student_app.services.grades.parse_student_grades(
                data.splitlines()
            )
            print("Оцінки як словник:", student_grades)
        finally:
            print("Спробу читання завершено")

    print("\n=== 3. Середній та прохідний бали ===")
    for total, count in (("270", "3"), ("270", "0"), ("помилка", "3")):
        try:
            result = student_app.services.grades.calculate_average(total, count)
            print(f"Середній бал: {result:.1f}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"{type(error).__name__}: {error}")

    print("Оцінка 85:", student_app.services.grades.check_passed(85))

    try:
        student_app.services.grades.check_with_log(45, str(log_file))
    except LowGradeError as error:
        print("Повторно перехоплено LowGradeError:", error)

    print("\nРоботу програми завершено")


if __name__ == "__main__":
    main()
