"""
Rot Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)

Version 3 (optional)
Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
"""

import string
user_input = input("Please enter a word: ")
rot_input = int(input("Enter encryption amount: "))

encoder = list(string.ascii_letters + string.digits + string.punctuation + " ")

# for i in range(len(user_input) - 1):
#     if user_input[i] in encoder:
#         try:
#             user_input[i] = encoder[i+rot]
#         except IndexError:

encrypted_input = []
for let in user_input:
    if let in encoder:
        alpha_index = encoder.index(let)
        rot = rot_input
        for i in encoder[alpha_index:]:
            if rot == 0:
                encrypted_input.append(i)
                break
            rot -= 1
            if encoder.index(i) == len(encoder) - 1:
                # if i == encoder[-1]:
                for i in encoder:
                    if rot == 0:
                        encrypted_input.append(i)
                        break
                    rot -= 1
    else:
        encrypted_input.append(let)

encrypted_input = "".join(encrypted_input)
print(encrypted_input)
