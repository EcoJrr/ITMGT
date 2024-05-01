'''Python: Intermediate

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    ascii_val = ord(letter) - ord('A')
    new_ascii_val = (ascii_val + shift) % 26
    return chr(new_ascii_val + ord('A'))

def caesar_cipher(message, shift):
    encrypted_message = ""
    for letter in message:
        encrypted_message += shift_letter(letter, shift)
    return encrypted_message

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    shift = ord(letter_shift) - ord('A')
    return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    encrypted_message = ""
    for i in range(len(message)):
        if message[i] != " ":
            shift = ord(key[i]) - ord('A')
            encrypted_message += shift_letter(message[i], shift)
        else:
            encrypted_message += " "
    return encrypted_message

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    encoded_message = ""
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[index]
    return encoded_message

def scytale_decipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    decoded_message = ""
    for i in range(len(message)):
        index = (i // (len(message) // shift)) + (shift * (i % (len(message) // shift)))
        decoded_message += message[index]
    return decoded_message

