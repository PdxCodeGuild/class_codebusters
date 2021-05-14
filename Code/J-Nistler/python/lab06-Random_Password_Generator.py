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
Version 1: 
Version 2: 

Future Improvements:

- 

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#

import string

# Define banks of character types in which to choose
punc_bank = string.punctuation
upper_bank = string.ascii_uppercase
lower_bank = string.ascii_lowercase
dig_bank = string.digits

# Solicit user input
input_pass_len = input("How many characters would you like your password? ")
input_num_upper = input("How many uppercase letters? ")
input_num_lower = input("How many lowercase letters? ")
input_num_dig = input("How many digits? ")



# for i in range(len(input_pass_len)):


