"""
Jared, Will, Iiron, Jorge, Kendall, Steve - TEAM 1
"""
import string


class RotCipher:

    def __init__(self, rot_amount):
        self.rot_amount = rot_amount
        self.letters = string.ascii_lowercase

    def encrypt(self, text):
        encrypted = ""
        for char in text:
            encrypted += self.letters[(self.letters.find(char) +
                                       self.rot_amount) % 26]
        return encrypted

    def decrypt(self, text):
        decrypted = ""
        for char in text:
            decrypted += self.letters[(self.letters.find(char) -
                                       self.rot_amount) % 26]
        return decrypted

    def __str__(self):
        return f'Rot{self.rot_amount} Cipher'


rot_cipher = RotCipher(7)

print(rot_cipher)

text = 'hello'

encrypted_text = rot_cipher.encrypt(text)

print(encrypted_text)  # uryyb
decrypted_text = rot_cipher.decrypt(encrypted_text)
print(decrypted_text)  # hello