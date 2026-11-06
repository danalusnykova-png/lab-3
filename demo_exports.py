"""Окрема демонстрація того, як працює __all__ у пакеті."""

import student_app

# import * дозволено тут лише для демонстрації __all__.
from student_app import *


if __name__ == "__main__":
    print("=== Демонстрація __all__ ===")
    print("Імена у student_app.__all__:", ", ".join(student_app.__all__))
    for name in student_app.__all__:
        print(f"{name} імпортовано: {name in globals()}")

    print("PACKAGE_INFO є у пакеті:", hasattr(student_app, "PACKAGE_INFO"))
    print("PACKAGE_INFO імпортовано через *:", "PACKAGE_INFO" in globals())
