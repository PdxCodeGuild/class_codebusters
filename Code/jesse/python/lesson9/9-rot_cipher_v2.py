'''
Allow the user to input the amount of rotation used in the encryption. (ROTN)
'''

import string

# list of lowercase alphabet
alphabet = list(string.ascii_lowercase)

# git ammount of ROT rotation from user
rot_input = int(input('Enter amount of rotation to be used in encryption: '))

# get string of letters from user, convert to lowercase and list
user_input = list(input('Enter a series of letters: ').lower())

# encrypt the user input string of letters using ROT
encrypted_input = []
for let in user_input:
    alpha_index = alphabet.index(let)
    rot = rot_input
    for i in alphabet[alpha_index:]:  
        if rot == 0:
            encrypted_input.append(i)
            break
        rot -= 1
        if alphabet.index(i) == 25:
            for i in alphabet:
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