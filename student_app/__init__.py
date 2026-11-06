"""Пакет для обробки оцінок студентів."""

from .models import StudentAppError, GradeValidationError, StudentFileError, LowGradeError

# Цей атрибут доступний як student_app.PACKAGE_INFO, але не через import *.
PACKAGE_INFO = "Навчальний пакет для практичної роботи"

# Саме ці імена потрапляють до from student_app import *.
__all__ = ["StudentAppError", "GradeValidationError", "StudentFileError", "LowGradeError"]
