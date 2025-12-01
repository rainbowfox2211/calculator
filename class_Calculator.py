import math


class Calculator:
    """Базовый класс калькулятора с арифметическими операциями."""
    
    def add(self, x, y):
        """Сложение"""
        return x + y

    def subtract(self, x, y):
        """Вычитание"""
        return x - y

    def multiply(self, x, y):
        """Умножение"""
        return x * y

    def divide(self, x, y):
        """Деление с проверкой на ноль"""
        if y == 0:
            raise ValueError("Ошибка: деление на ноль!")
        return x / y

    def power(self, x, y):
        """Возведение в степень"""
        return x ** y

    def sqrt(self, x):
        """Квадратный корень"""
        if x < 0:
            raise ValueError("Ошибка: корень из отрицательного числа!")
        return math.sqrt(x)

    def percentage(self, x, y):
        """Процент от числа (x% от y)"""
        return (x / 100) * y