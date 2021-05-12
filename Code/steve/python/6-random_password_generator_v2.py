"""
Random Password Generator
Part 1

Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. 
Allow the user to enter the value of n, remember to convert its type to an int, 
as input returns a string. Hint: random.choice can be used to pick a character 
out of a string, as well as an element out of a list.

Part 2 (optional)

Ask the user for how many lowercase letters, uppercase letters, 
numbers, and special characters they'd like in their password. 
You do not want the pieces in order (e.g. 3 lowercase letters followed 
by 3 uppercase letters...). You can use list(password_string) 
or password_string.split('') to convert the string to a list, 
random.shuffle(password_list) to shuffle it, and then ''.join(password_list) 
to turn it back into a string.
"""
import random
import string


# get user input and generate password
def get_pwd_input():
    pwd = ''
    passes = 0
    while passes < 4:
        char = ''
        if passes == 0:
            char = 'lowercase'
            n = get_pwd_len(char)
            pwd_lower = ''
            c = 0
            while c < n:
                pwd_lower += random.choice(string.ascii_lowercase)
                c += 1
        elif passes == 1:
            char = 'uppercase'
            n = get_pwd_len(char)
            pwd_upper = ''
            c = 0
            while c < n:
                pwd_upper += random.choice(string.ascii_uppercase)
                c += 1
        elif passes == 2:
            char = 'number'
            n = get_pwd_len(char)
            pwd_num = ''
            c = 0
            while c < n:
                pwd_num += random.choice(string.digits)
                c += 1
        else:
            char = 'punctuation'
            n = get_pwd_len(char)
            pwd_punc = ''
            c = 0
            while c < n:
                pwd_punc += random.choice(string.punctuation)
                c += 1
        passes += 1
    pwd = pwd_lower + pwd_upper + pwd_num + pwd_punc
    pwd_list = list(pwd)
    random.shuffle(pwd_list)
    pwd = ''.join(pwd_list)

    return f'Your password is: {pwd}'


# create a function to validate user input
def get_pwd_len(char):
    while True:
        pwd_len = input(
            f'Enter the number of {char} characters for your password: ')
        try:
            if int(pwd_len) and int(pwd_len) >= 0:
                pwd_len = int(pwd_len)
                break
            else:
                print('Enter a valid password number.')
        except ValueError:
            print('Enter a valid password number.')
    return pwd_len


if __name__ == '__main__':
    print(get_pwd_input())
