"""Набор тестов для кодирования и декодирование шифром Цезаря. """

import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CeasarTestCase(unittest.TestCase):
    """ Тесты """

    def test_encrypt(self) -> None:
        self.assertEqual(encrypt_caesar("PYTHON3.6"), "SBWKRQ3.6")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("SBWKRQ3.6"),"PYTHON3.6")

    def test_not_latin_script(self):
        with self.assertRaises(ValueError):
            encrypt_caesar('Клад едет в Рим')

    def test_register(self):
        self.assertEqual(encrypt_caesar('PyThOn iS GoOd'),"SbWkRq lV JrRg")

    def test_last_letters_alf(self):
        self.assertEqual(encrypt_caesar('ZYX'),"CBA")

    def test_not_letters(self):
        self.assertEqual(encrypt_caesar('123!?'),"123!?")