import string


def caesarCipherEncryptor(input_str, key):
    letters = string.ascii_lowercase
    encrypted = ''
    for char in input_str:
        encrypted += letters[(letters.index(char) + key) % len(letters)]
    return encrypted
