"""
Part 1
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
"""

import random
from string import ascii_lowercase, ascii_uppercase, digits as numbers, punctuation


def version1():
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        try:
            pw_length = int(input("How long do you want you password to be? "))
            break
        except ValueError:
            print("Enter a number.")

    password = ""
    while len(password) < pw_length:
        password += random.choice(characters)

    print(password)


# version1()
"""
Part 2 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.
"""


def validate_int(message):
    while True:
        try:
            length = int(input(f"How many {message}: "))
            break
        except ValueError:
            print("Enter a number.")

    return length


def version2():

    pw_length = validate_int("characters")
    lowercase = validate_int("lowercase")
    uppercase = validate_int("uppercase")
    digits = validate_int("digits")
    special = validate_int("special characters")

    password = ""
    count = 0
    lower_count = 0
    upper_count = 0
    number_count = 0
    spec_char_count = 0

    while count < pw_length:
        if lower_count < lowercase:
            password += random.choice(ascii_lowercase)
            lower_count += 1
        elif upper_count < uppercase:
            password += random.choice(ascii_uppercase)
            upper_count += 1
        elif number_count < digits:
            password += random.choice(numbers)
            number_count += 1
        elif spec_char_count < special:
            password += random.choice(punctuation)
            spec_char_count += 1
        count += 1

    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    print(password)


version2()
