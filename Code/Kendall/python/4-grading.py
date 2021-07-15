'''
Part 1
Let's convert a number grade to a letter grade, using if and elif statements and comparisons. 
First have the user enter a number representing the grade (0-100). 
Then convert the number grade to a letter grade.

Part 2
Find the specific letter grade (A+, B-, etc). 
You can check for more specific ranges using if statements, or use modulus % 
to get the ones-digit to set another string to '+', '-', or ' '. 
Then you can concatenate that string with your grade string.
'''

import utils


# Getting user input
num = utils.get_int("Enter your score: ")

# Determining if the Grade is +, - or neither
if num % 10 > 6:
    sign = '+'
elif num % 10 < 4:
    sign = '-'
else:
    sign = ' '

# Defining grades ranges using if and elif statements
if 90 <= num <= 100:
    print(f'A{sign}')
elif 80 <= num < 90:
    print(f'B{sign}')
elif 70 <= num < 80:
    print(f'C{sign}')
elif 60 <= num < 70:
    print(f'D{sign}')
elif num < 60:
    print('F')
