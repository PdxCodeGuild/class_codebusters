'''

Rot Cipher

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
Version 2

Allow the user to input the amount of rotation used in the encryption. (ROTN)

Version 3 (optional)

Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.

'''
# # Version 1

# import string

# # Prompt user for a word to be encoded
# user_input = input('Please enter a word: ')

# # Create string of lowercase alpha chars
# encoder = list(string.ascii_lowercase)

# # Set ROT13 var to 13
# rot13 = 13

# # Encode user input with ROT13
# encoded_input = ''
# # Loop through the range of length of the user's input
# for i in range(len(user_input)):
#     # Set a code var to compare indices of user_input chars to
#      # indices of first occurences of char in encoder list
#      # adding the rot13 count, and modulus that by 26
#     code = (encoder.index(user_input[i]) + rot13) % 26
#     # add the encoded char to the encoded_input string
#     encoded_input += encoder[code]

# print(encoded_input) #print the encoded input

# Version 2

import string

user_input = input('Please enter a word to encrypt: ')
rotn = int(input('Please enter the (ROTN) number of rotations: '))

encoder = list(string.ascii_lowercase)

encoded_input = ''

for i in range(len(user_input)):

    code = (encoder.index(user_input[i]) + rotn) % 26
    encoded_input += encoder[code]

print(encoded_input)
