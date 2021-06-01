'''
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
'''
import string

# list of lowercase alphabet
alphabet = list(string.ascii_lowercase)

# get string of letters from user, convert to lowercase and list
user_input = list(input('Enter a series of letters: ').lower())

# encrypt the user input string of letters using ROT
encrypted_input = []
for let in user_input:
    alpha_index = alphabet.index(let)
    rot = 13
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