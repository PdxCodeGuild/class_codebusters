'''

Random Password Generator

Part 1

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Part 2 (optional)

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.

'''

# Part 1 

import random
import string

# ask user to enter number length for password
user_pw_length = int(input('Enter desired number of characters for your password: '))

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
digits = string.digits
punc = string.punctuation
blank = string.whitespace

valid_chars = upper_letters + lower_letters + digits + punc + blank

password = ''

i = 0

while i < user_pw_length:
    i += 1
    password += random.choice(valid_chars)

print(password)