import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    j = 0
    shifts = []
    ciphertext = ""
    alf = "abcdefghijklmnopqrstuvwxyz"
    for i in keyword:
        if i.isupper():
            shift = ord(i.lower()) - 97
            shifts.append(shift)
        else:
            shift = ord(i) - 97
            shifts.append(shift)
    for letter in plaintext:
        if letter not in string.ascii_letters:
            ciphertext += letter
        else:
            if letter.islower():
                shift = j % len(shifts)
                letter_shift = alf[((alf.index(letter) + shifts[shift]) % 26)]
                ciphertext += letter_shift
                j += 1
            else:
                shift = j % len(shifts)
                letter_shift = alf[((alf.index(letter.lower()) + shifts[shift]) % 26)].upper()
                ciphertext += letter_shift
                j += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    j = 0
    shifts = []
    alf = "abcdefghijklmnopqrstuvwxyz"
    for i in keyword:
        if i.isupper():
            shift = ord(i.lower()) - 97
            shifts.append(shift)
        else:
            shift = ord(i) - 97
            shifts.append(shift)
    for letter in ciphertext:
        if letter not in string.ascii_letters:
            plaintext += letter
        else:
            if letter.islower():
                shift = j % len(shifts)
                letter_shift = alf[((alf.index(letter) - shifts[shift]) % 26)]
                plaintext += letter_shift
                j += 1
            else:
                shift = j % len(shifts)
                letter_shift = alf[((alf.index(letter.lower()) - shifts[shift]) % 26)].upper()
                plaintext += letter_shift
                j += 1
    return plaintext
