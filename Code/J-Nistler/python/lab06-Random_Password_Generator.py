#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 03
Lab 06 - Random Password Generator
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Part 1
Let's generate a password of length n using a while 
loop and random.choice, this will be a string of random 
characters, e.g. a62xB95. Allow the user to enter the 
value of n, remember to convert its type to an int, as 
input returns a string. Hint: random.choice can be used 
to pick a character out of a string, as well as an element 
out of a list.

Part 2 (optional)
Ask the user for how many lowercase letters, uppercase 
letters, numbers, and special characters they'd like 
in their password. You do not want the pieces in order 
(e.g. 3 lowercase letters followed by 3 uppercase letters...). 
You can use list(password_string) or password_string.split('') 
to convert the string to a list, random.shuffle(password_list) 
to shuffle it, and then ''.join(password_list) to turn it back 
into a string.
'''

#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: Complete

Future Improvements:
- 

'''
#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#

# import necessary dependencies
import random
import string

#-----------------------------------------------#
# Create Neccesary Objects
#-----------------------------------------------#

# Creates character banks for each character type
lower_bank = string.ascii_lowercase
upper_bank = string.ascii_uppercase
digit_bank = string.digits
symbol_bank = string.punctuation

# create a string in which to store the generated password
password = ""

#-----------------------------------------------#
# Input from User
#-----------------------------------------------#
# LENGTH OF PASSWORD
while True:
# recieves input from user on password length
    num_upper = input("How many upper-case letters? ")
# convert user input to int
    try:
        num_upper = int(num_upper)
        break
    except TypeError:
        print("Please input a valid integer")
        continue

# NUMBER OF LETTERS
while True:
    # prompts user for number of letters
    num_lower = input("How many lower-case letters? ")
    try:
        # convert user input to int
        num_lower = int(num_lower)
        break
    except TypeError:
        print("Please input a valid integer")
        continue

# NUMBER OF DIGITS
while True:
    # prompts user for number of digits
    num_digit = input("How many digits? ")
    try:
        # convert user input to int
        num_digit = int(num_digit)
        break
    except TypeError:
        print("Please input a valid integer")
        continue

# NUMBER OF SYMBOLS
while True:
    # prompts user for number of digits
    num_sym = input("How many symbols? ")
    try:
        # convert user input to int
        num_sym = int(num_sym)
        break
    except TypeError:
        print("Please input a valid integer")
        continue

#-----------------------------------------------#
# Add characters to Password
#-----------------------------------------------#

# defines a function that takes in the character source and number of 
# characters to generate, then returns those characters in a string.
def pass_gen (char_source, num):
    # create counter
    counter = 0
    pass_seg = ""
    # adds specified number of character type to the password
    while counter < num:
        # adds random character to the password segment from the character bank
        pass_seg += random.choice(char_source)
        # marks the counter
        counter += 1
    return pass_seg

#-----------------------------------------------#
# Construct Password
#-----------------------------------------------#

# calls on the pass_gen function to generate the appropriate character type
# and number of symbols as specified by the user. Concatenates into one string
password = pass_gen(upper_bank, num_upper) + pass_gen(lower_bank, num_lower) + pass_gen(digit_bank, num_digit) + pass_gen(symbol_bank, num_sym)
# convert password string to list
password = list(password)
# jumble password characters
random.shuffle(password)
# re-assemble characters into string
password = ''.join(password)

#-----------------------------------------------#
# Print Password
#-----------------------------------------------#

# prints generated password for the user
print(f'''
--------------------
Generated password: {password}
--------------------
''')