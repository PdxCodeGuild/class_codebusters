import random
import string
characters = string.ascii_lowercase  # gets characters for the password
characters += string.ascii_uppercase
characters += string.digits
characters += string.punctuation

# gets users desired password length
n = input('How many characters would you like in your password? ')
n = int(n)  # converts input to integer
while n > 0:
    for i in range(n):
        password = str(random.choice(characters))
        print(password)
        n -= 1
