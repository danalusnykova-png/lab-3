"""Демонстрація help() і атрибутів документації в Python."""

from student_app.models import GradeValidationError
from student_app.services.grades import parse_grade, parse_student_grades


def main() -> None:
    """Вивести документацію та анотації обраних функцій і класу.

    Args:
        Немає: Функція не приймає параметрів.

    Returns:
        None: Дані виводяться в консоль.

    Raises:
        Немає: Використовується тільки читання метаданих об'єктів.
    """
    print("=== 1. Виклик help(parse_grade) ===")
    help(parse_grade)

    print("\n=== 2. Атрибути функції ===")
    print("__name__:", parse_grade.__name__)
    print("__doc__:\n", parse_grade.__doc__)
    print("__annotations__:", parse_grade.__annotations__)

    print("\n=== 3. Параметризовані типи ===")
    print("__name__:", parse_student_grades.__name__)
    print("__annotations__:", parse_student_grades.__annotations__)

    print("\n=== 4. Документація власного виключення ===")
    print("Клас:", GradeValidationError.__name__)
    print("Опис:", GradeValidationError.__doc__.strip().splitlines()[0])


if __name__ == "__main__":
    main()
