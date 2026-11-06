# Базовий клас для всіх помилок програми
class StudentAppError(Exception):
    pass


# Помилка введення оцінки
class GradeValidationError(StudentAppError):
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def __str__(self):
        return f"Неправильне значення поля '{self.field}': {self.value}"


# Помилка роботи з файлом
class StudentFileError(StudentAppError):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f"Не вдалося знайти файл '{self.filename}'"


# Помилка, якщо студент не набрав прохідний бал
class LowGradeError(StudentAppError):
    def __init__(self, grade, minimum):
        self.grade = grade
        self.minimum = minimum

    def __str__(self):
        return f"Оцінка {self.grade} нижча за прохідний бал {self.minimum}"


# Перевірка введеної оцінки
def parse_grade(value):
    try:
        grade = int(value)
    except (ValueError, TypeError):
        raise GradeValidationError("оцінка", value)

    if grade < 0 or grade > 100:
        raise GradeValidationError("оцінка", value)

    return grade


# Читання оцінок з файлу
def read_grades(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as error:
        raise StudentFileError(filename) from error


# Перевірка прохідного бала
def check_passed(grade, minimum=60):
    if grade < minimum:
        raise LowGradeError(grade, minimum)

    return "Студент склав предмет"


# Запис помилки у журнал і повторне піднесення
def check_with_log(grade):
    try:
        return check_passed(grade)
    except LowGradeError as error:
        with open("student_errors.log", "a", encoding="utf-8") as file:
            file.write(str(error) + "\n")

        print("Помилку записано у student_errors.log")
        raise


def main():
    print("=== 1. Помилка перевірки оцінки ===")
    print("Правильне значення:", parse_grade("88"))

    try:
        parse_grade("невідомо")
    except GradeValidationError as error:
        print("Перехоплено GradeValidationError:", error)

    # Перехоплення через базовий клас
    try:
        parse_grade("120")
    except StudentAppError as error:
        print("Перехоплено через StudentAppError:", error)

    print("\n=== 2. Помилка роботи з файлом ===")

    with open("student_grades_task2.txt", "w", encoding="utf-8") as file:
        file.write("Настя: 95\nДана: 92\nПетя: 76\n")

    print("Успішне читання файлу:")
    print(read_grades("student_grades_task2.txt").strip())

    try:
        read_grades("missing_folder/student_grades_task2.txt")
    except StudentFileError as error:
        print("Перехоплено StudentFileError:", error)
        print("Початкова причина:", type(error.__cause__).__name__)

    print("\n=== 3. Перевірка прохідного бала ===")
    print("Оцінка 85:", check_passed(85))

    try:
        check_with_log(45)
    except LowGradeError as error:
        print("Повторно перехоплено LowGradeError:", error)


if __name__ == "__main__":
    main()

