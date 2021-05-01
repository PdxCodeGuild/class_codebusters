# Random Password Generator
# Part 1
# Let's generate a password of length n using a while loop and random.choice, this will be a string 
# of random characters, e.g. a62xB95. Allow the user to enter the value of n, remember to convert its 
# type to an int, as input returns a string. Hint: random.choice can be used to pick a character out 
# of a string, as well as an element out of a list.
import random
'''
allChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

def generatePassword(n):
    i = 0
    password = ''
    while i < n:
        password += random.choice(allChar)
        i += 1
    return password


userInput = int(input("Please enter the length of password: "))
print(generatePassword(userInput))
'''

# Part 2 (optional)
# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters 
# they'd like in their password. You do not want the pieces in order (e.g. 3 lowercase letters followed 
# by 3 uppercase letters...). You can use list(password_string) or password_string.split('') to convert 
# the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to 
# turn it back into a string.

low = 'abcdefghijklmnopqrstuvwxyz'
ups = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '0123456789!@#$%^&*()'

def generatePassword(l,u,s):
    i = 0
    password = ''
    while i < l:
        password += random.choice(low)
        i += 1
    i = 0
    while i < u:
        password += random.choice(ups)
        i += 1
    i = 0
    while i < s:
        password += random.choice(special)
        i += 1
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


lowers = int(input("Please enter how many lowercase characters in password: "))
uppers = int(input("Please enter how many uppercase characters in password: "))
specials = int(input("Please enter how many special characters in password: "))
print(generatePassword(lowers,uppers,specials))

