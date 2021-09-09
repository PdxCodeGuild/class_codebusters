'''
Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
'''

import string

# list of lowercase alphabet
characters = list(string.ascii_letters + string.digits + string.punctuation)

# git ammount of ROT rotation from user
rot_input = int(input('Enter amount of rotation to be used in encryption: '))

# get string of letters from user, convert to lowercase and list
user_input = list(input('Enter a series of letters: ').lower())

# encrypt the user input string of letters using ROT
encrypted_input = []
for let in user_input:
    alpha_index = characters.index(let)
    rot = rot_input
    for i in characters[alpha_index:]:  
        if rot == 0:
            encrypted_input.append(i)
            break
        rot -= 1
        if i == characters[-1]:
            for i in characters:
                if rot == 0:
                    encrypted_input.append(i)
                    break
                rot -= 1
encrypted_input = ''.join(encrypted_input)

# for let in user_input:
#     alpha_index = alphabet.index(let)
#     rot = 13
#     rotation = (alpha_index + rot) % 26

print(encrypted_input)