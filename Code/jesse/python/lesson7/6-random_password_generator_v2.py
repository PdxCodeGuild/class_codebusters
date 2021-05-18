'''
Part 2 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.
'''

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


# function to keep asking for user input until a valid number is entered.
# convert to int and return as int if valid
def validate_int(message):
    while True:
        try:
            length = int(input(f'How many {message}? '))
            break
        except ValueError:
            print('Try again.')
    return length

# get length of password and individual character lengths from user and run through function
pass_length = validate_int('total characters')
num_lower_let = validate_int('lowercase letters')
num_upper_let = validate_int('uppercase letters')
num_numbers = validate_int('numbers')
num_spec_char = validate_int('special characters')

password = ''

# keep track of the overall number of password characters as well as the the number of each character type
count = 0
lower_count = 0
upper_count = 0
number_count = 0
spec_char_count = 0

# randomly select characters from each character type until password length is reached.
while count < pass_length:

# each character type is added only if it has not yet reached the limit set by the user for that type
    if lower_count < num_lower_let:
        password += random.choice(ascii_lowercase)
        lower_count += 1
    elif upper_count < num_upper_let:
        password += random.choice(ascii_uppercase)
        upper_count += 1 
    elif number_count < num_numbers:
        password += random.choice(digits)
        number_count += 1 
    elif spec_char_count < num_spec_char:
        password += random.choice(punctuation)
        spec_char_count += 1

# if the overall character limit set by the player is reached, password creation will be cut off even if 
# the sum of the individual character type limits are higher than the overall limit.
    count += 1

# put the password in random order
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(password)