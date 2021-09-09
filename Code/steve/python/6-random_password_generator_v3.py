
import random
import string


# create a function to get and validate user input
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


def gen_pwd():
    char_list = ['lowercase', 'uppercase', 'digits', 'punctuation']
    pwd = ''
    for char in char_list:
        n = get_pwd_len(char)
        c = 0
        if char == 'lowercase':
            while c < n:
                pwd += random.choice(string.ascii_lowercase)
                c += 1
        if char == 'uppercase':
            while c < n:
                pwd += random.choice(string.ascii_uppercase)
                c += 1
        if char == 'digits':
            while c < n:
                pwd += random.choice(string.digits)
                c += 1
        if char == 'punctuation':
            while c < n:
                pwd += random.choice(string.punctuation)
                c += 1

    pwd_list = list(pwd)
    random.shuffle(pwd_list)
    pwd = ''.join(pwd_list)

    return f'Your password is: {pwd}'


if __name__ == '__main__':
    print(gen_pwd())
