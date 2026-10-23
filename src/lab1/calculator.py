"""Модуль с реализацией класса Calculator."""


class Calculator:
    """Калькулятор с базовыми арифметическими операциями."""

    def division(self, a: float, b: float) -> float:
        """операция деления."""
        return a / b

    def add(self, a: float, b: float) -> float:
        """операция сложения."""
        return a + b

    def subtraction(self, a: float, b: float) -> float:
        """операция вычитания."""
        return a - b

    def multiplication(self, a: float, b: float) -> float:
        """операция умножения."""
        return a * b

    def exponentiation(self, a: float, b: float) -> float:
        """операция возведения в степень."""
        return a**b
