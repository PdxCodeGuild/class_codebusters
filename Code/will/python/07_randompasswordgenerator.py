#import random
import random
#import string
import string
# input statement for the user and define it as "n". Conver n into a integer
n = int(input('Enter the length of the password: '))

# list of letters and numbers
characters = string.ascii_letters + string.digits

# empty string for password
password = []

# for loop to draw random letters and numbers
for x in range(n):
    password.append(random.choice(characters))
print(''.join(password))
