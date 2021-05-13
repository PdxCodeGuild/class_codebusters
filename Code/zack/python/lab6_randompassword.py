'''
COMMENTED OUT. WHILE PART 2 RUNS
# # # PART 1 # # #
#imports
import random
import string 

#random choice values
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0]
values = list(string.ascii_letters)
values.extend(nums)

#defining password length
n = input('Enter password length: ')
n = int(n)

#password value
password = ''

#iterable
i = 0

#password's character assignment
while i <= n:
    #adding a random value
    password += random.choice(values)
    #cycling through to the next position
    i += 1

#Output upon password completion
if i > n:
    print(f'Your password is {password}')
'''


# # # PART 2 # # #
import random
import string

# random choice values
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
uppers = list(string.ascii_uppercase)
lowers = list(string.ascii_lowercase)

# user input
nums_check = input('Enter number of password numbers: ')
uppers_check = input('Enter number of password capital letters: ')
lowers_check = input('Enter number of password letters: ')

# inting
nums_check = int(nums_check)
uppers_check = int(uppers_check)
lowers_check = int(lowers_check)

# obtain values
thevalues = []
i = 0
while i <= nums_check:
    thevalues += random.choice(nums)
    i += 1

i = 0
while i <= uppers_check:
    thevalues += random.choice(uppers)
    i += 1

i = 0
while i <= lowers_check:
    thevalues += random.choice(lowers)
    i += 1

random.shuffle(thevalues)
password = ''.join(thevalues)

print(f'Your password is {password}')
