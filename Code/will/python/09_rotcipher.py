'''
Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.
'''

# Version 1
# input statement  letters
# import string
# letters = string.ascii_lowercase

# # user input statement
# user_input = input('Enter a string: ')


# # function that moves each letter 13 positions in the alphabet


# def rot13(user_input):
#     encrypted = " "

#     for char in user_input:
#         encrypted += letters[(letters.find(char)+13) % 26]
#     return encrypted


# print(rot13(user_input))


# Version 2
# input statement  letters
import string
letters = string.ascii_lowercase

# user input statement
user_input = input('Enter a string: ')
rotations = int(input('Enter rotations: '))

# function that moves each letter 13 positions in the alphabet


def rot13(user_input):
    encrypted = " "

    for char in user_input:
        encrypted += letters[(letters.find(char)+rotations) % 26]
    return encrypted


print(rot13(user_input))
