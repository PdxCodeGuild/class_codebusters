'''
Mob Lab - Rot Cipher Classes
Calen, Jesse, Neil, Richard, and Zack

'''
import string

alphabet = list(string.ascii_lowercase)


class RotCipher:

    def __init__(self, rot_amount):
        self.rot_amount = rot_amount

    def encrypt(self, text):
        result = ''

        for i in range(len(text)):
            rotation = (alphabet.index(text[i]) + self.rot_amount) % 26
            result += alphabet[rotation]
        return result

    def decrypt(self, text):
        result = ''

        for i in range(len(text)):
            rotation = (alphabet.index(text[i]) - self.rot_amount) % 26
            result += alphabet[rotation]
        return result

    def __str__(self):
        return str(self.rot_amount)


rot_cipher = RotCipher(10)

text = 'mcdonalds'
encrypted_text = rot_cipher.encrypt(text)
print(encrypted_text)  # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text)  # hello
print(rot_cipher)
