#import random
import random
#import string
import string
# input statement for the user and define it as "n". Conver n into a integer
pw_length = int(input('Enter the length of the password: '))

# list of letters and numbers
characters = string.ascii_letters + string.digits

# empty string for password
password = ""

# for loop to draw random letters and numbers
while len(password) < pw_length:
    password += random.choice(characters)

print(password)
