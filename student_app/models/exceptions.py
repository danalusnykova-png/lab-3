"""Власні виключення для обробки оцінок студентів.

Модуль містить базовий клас помилок і три його підкласи.
"""


class StudentAppError(Exception):
    """Базова помилка програми для роботи з оцінками.

    Args:
        message (str): Текст помилки. За замовчуванням порожній рядок.

    Returns:
        StudentAppError: Об'єкт виключення.

    Raises:
        Немає: Саме створення об'єкта не викликає помилок.
    """

    def __init__(self, message: str = "") -> None:
        """Зберегти повідомлення про помилку.

        Args:
            message (str): Повідомлення для користувача.

        Returns:
            None: Метод нічого не повертає.

        Raises:
            Немає: Помилки не піднімаються.
        """
        super().__init__(message)


class GradeValidationError(StudentAppError):
    """Помилка неправильного значення оцінки.

    Args:
        field (str): Назва поля з помилкою.
        value (object): Введене неправильне значення.

    Returns:
        GradeValidationError: Об'єкт помилки перевірки оцінки.

    Raises:
        Немає: Створення об'єкта не піднімає виключень.
    """

    def __init__(self, field: str, value: object) -> None:
        """Зберегти назву поля та його неправильне значення.

        Args:
            field (str): Назва поля.
            value (object): Значення, яке не пройшло перевірку.

        Returns:
            None: Метод нічого не повертає.

        Raises:
            Немає: Помилки не піднімаються.
        """
        self.field = field
        self.value = value
        super().__init__(str(self))

    def __str__(self) -> str:
        """Повернути зрозуміле повідомлення про неправильну оцінку.

        Args:
            Немає: Метод використовує атрибути об'єкта.

        Returns:
            str: Опис неправильного поля та його значення.

        Raises:
            Немає: Помилки не піднімаються.
        """
        return f"Неправильне значення поля '{self.field}': {self.value}"


class StudentFileError(StudentAppError):
    """Помилка відсутнього файлу з оцінками.

    Args:
        filename (str): Шлях до файлу, який не вдалося відкрити.

    Returns:
        StudentFileError: Об'єкт помилки роботи з файлом.

    Raises:
        Немає: Створення об'єкта не піднімає виключень.
    """

    def __init__(self, filename: str) -> None:
        """Зберегти шлях до відсутнього файлу.

        Args:
            filename (str): Назва або шлях до файлу.

        Returns:
            None: Метод нічого не повертає.

        Raises:
            Немає: Помилки не піднімаються.
        """
        self.filename = filename
        super().__init__(str(self))

    def __str__(self) -> str:
        """Повернути повідомлення про відсутній файл.

        Args:
            Немає: Метод використовує атрибут filename.

        Returns:
            str: Текст із назвою відсутнього файлу.

        Raises:
            Немає: Помилки не піднімаються.
        """
        return f"Не вдалося знайти файл '{self.filename}'"


class LowGradeError(StudentAppError):
    """Помилка, коли оцінка нижча за прохідний бал.

    Args:
        grade (int): Оцінка студента.
        minimum (int): Мінімальна прохідна оцінка.

    Returns:
        LowGradeError: Об'єкт помилки низької оцінки.

    Raises:
        Немає: Створення об'єкта не піднімає виключень.
    """

    def __init__(self, grade: int, minimum: int) -> None:
        """Зберегти оцінку та прохідний бал.

        Args:
            grade (int): Оцінка, яку отримав студент.
            minimum (int): Мінімальна допустима оцінка.

        Returns:
            None: Метод нічого не повертає.

        Raises:
            Немає: Помилки не піднімаються.
        """
        self.grade = grade
        self.minimum = minimum
        super().__init__(str(self))

    def __str__(self) -> str:
        """Повернути повідомлення про низьку оцінку.

        Args:
            Немає: Метод використовує атрибути об'єкта.

        Returns:
            str: Повідомлення з оцінкою та прохідним балом.

        Raises:
            Немає: Помилки не піднімаються.
        """
        return f"Оцінка {self.grade} нижча за прохідний бал {self.minimum}"
