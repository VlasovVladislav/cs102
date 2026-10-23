""" Модуль с реализацией шифра Цезаря """

import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    if any(i not in string.printable for i in plaintext):
        raise ValueError("Error, encrypt_caesar may contains only Latin script")
    ciphertext = ""
    alf = "abcdefghijklmnopqrstuvwxyz"
    for letter in plaintext:
        if letter not in string.ascii_letters:
            ciphertext += letter
        else:
            if letter.islower():
                letter_cesar = alf[((alf.index(letter) + shift) % 26)]
                ciphertext += letter_cesar
            else:
                letter_cesar = (alf[((alf.index(letter.lower()) + shift) % 26)]).upper()
                ciphertext += letter_cesar
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    plaintext = encrypt_caesar(ciphertext, -shift)
    return plaintext
