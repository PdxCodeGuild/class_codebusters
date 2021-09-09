"""
Rot Cipher

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the
corresponding character, add it to an output string. Notice that there are 26 letters in the English language,
so encryption is the same as decryption.
Index 	0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25
English a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z
ROT+13 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z 	a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m
"""

# set length variables
n = 13
x = 26 - n

# get plain text from user
txt = input('Enter a sentence to encipher: ')

# iterate over the input and create the rot13 cipher


def to_cipher(txt):
    cip_txt = ''
    for char in txt:
        if ord(char) < 97 or ord(char) > 122:
            cip_txt += (chr(ord(char)))
        elif ord(char) >= 97 + x:
            cip_txt += (chr(ord(char) - x))
        else:
            cip_txt += (chr(ord(char) + n))
    return cip_txt

# iterate over the cipher string to return it to plain text


def to_text(p_txt):
    plain_txt = ''
    for char in p_txt:
        if ord(char) < 97 or ord(char) > 122:
            plain_txt += (chr(ord(char)))
        elif ord(char) <= 122 - x:
            plain_txt += (chr(ord(char) + x))
        else:
            plain_txt += (chr(ord(char) - n))
    return plain_txt


if __name__ == '__main__':
    p_txt = to_cipher(txt)
    print(p_txt)
    print(to_text(p_txt))
