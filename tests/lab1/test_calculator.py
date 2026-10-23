"""Набор тестов для класса Calculator. """

import unittest

from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    """ Тесты """
    def setUp(self):
        """ Создать калькулятор перед каждым тестом """
        self.calc = Calculator()

    def test_division(self):
        """ Проверка операции деления """
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_division_zero(self):
        """ Проверка деления на ноль """
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(10, 0)

    def test_add(self):
        """ Проверка операции сложения """
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        """ Проверка операции вычитания """
        self.assertEqual(self.calc.subtraction(10, 2),8)

    def test_multiplication(self):
        """ Проверка операции умножения """
        self.assertEqual(self.calc.multiplication(10, 8), 80)

    def test_exponentiation(self):
        """ Проверка операции возведения в степень """
        self.assertEqual(self.calc.exponentiation(2,5),32)
