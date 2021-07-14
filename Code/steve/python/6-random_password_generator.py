"""
Random Password Generator
Part 1

Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. 
Allow the user to enter the value of n, remember to convert its type to an int, 
as input returns a string. Hint: random.choice can be used to pick a character 
out of a string, as well as an element out of a list.
"""
import random
import string


# get and validate password length input from user
def get_pwd_len():
    while True:
        pwd_len = input('Enter the number of characters for your password: ')
        try:
            if int(pwd_len) and int(pwd_len) >= 0:
                pwd_len = int(pwd_len)
                break
            else:
                print('Enter a valid password number.')
        except ValueError:
            print('Enter a valid password number.')
    return pwd_len


# generate a random password using Alpha Numeric characters
def gen_pwd():
    n = get_pwd_len()
    # + string.punctuation ## for future use
    pwd_string = string.ascii_letters + string.digits
    c = 0
    pwd = ''
    while c < n:
        pwd += random.choice(pwd_string)
        c += 1
    return f'Here is your {n} character password: {pwd}'


if __name__ == '__main__':
    print(gen_pwd())
