from random import choice
import string
characters = string.ascii_lowercase  # gets characters for the password
characters += string.ascii_uppercase
characters += string.digits
characters += string.punctuation


# gets users desired password length
n = input('How many characters would you like in your password? ')
n = int(n)  # converts input to integer
password = []  # blank list to pass random choices to
while n > 0:  # while loop ensures a positive number is given
    for i in range(n):  # passes input
        password.append(choice(characters))  # adds random choices to list
        n -= 1  # stops cycle at selected number
# Converts list to string and prints
print("your password is " + ''.join(password))
