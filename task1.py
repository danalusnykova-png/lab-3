# Сценарій 1. Проста конструкція try/except
def check_grade(value):
    print(f"Введена оцінка: {value}")

    try:
        grade = int(value)
        if grade < 0 or grade > 100:
            raise ValueError("Оцінка має бути від 0 до 100")
        print(f"Успішно: оцінка {grade} правильна")
    except ValueError as error:
        print(f"Помилка ValueError: {error}")


# Сценарій 2. Повна конструкція та with
def read_grades(filename):
    print(f"Читаємо файл: {filename}")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        print("Помилка FileNotFoundError: файл не знайдено")
    else:
        print("Успішно: файл прочитано")
        print(data.strip())
    finally:
        print("Блок finally: спробу читання завершено")


# Сценарій 3. Перехоплення кількох типів помилок
def calculate_average(total, count):
    print(f"Сума оцінок: {total}, кількість: {count}")

    try:
        total = int(total)
        count = int(count)
        average = total / count
        print(f"Успішно: середній бал = {average:.1f}")
    except (ValueError, ZeroDivisionError) as error:
        print(f"Помилка {type(error).__name__}: {error}")


def main():
    print("=== Сценарій 1. try/except ===")
    check_grade("88")
    check_grade("невідомо")

    print("\n=== Сценарій 2. try/except/else/finally + with ===")

    # Створення файлу з оцінками
    with open("student_grades.txt", "w", encoding="utf-8") as file:
        file.write("Настя: 95\nДана: 92\nПетя: 76\n")

    read_grades("student_grades.txt")
    read_grades("missing_folder/student_grades.txt")

    print("\n=== Сценарій 3. except (ValueError, ZeroDivisionError) ===")
    calculate_average("270", "3")
    calculate_average("270", "0")
    calculate_average("помилка", "3")


if __name__ == "__main__":
    main()

