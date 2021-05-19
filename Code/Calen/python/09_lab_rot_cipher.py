'''
    Write a program that prompts the user for a string, 
    and encodes it with ROT13. For each character, find the corresponding character, 
    add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

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

# set perams.

index_adjustmnet = 0

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]


# get input
while True:
    user_input = input('Please advise on rot number: ')
    try:
        user_input = int(user_input)
    
    except ValueError:
        pass

    if type(user_input) == int:
        index_adjustmnet += user_input # did not know if there was a version of .copy() used on lists, but for ints. so used += as by default index = 0 via line 24
        break

# process input

non_coded_text = list(input(f'please insert your text, rot selected is {index_adjustmnet}:  '))

for i in range(len(non_coded_text)-1):
    if non_coded_text[i] in alph:
        try:
            non_coded_text[i] = alph[i+index_adjustmnet]
        except IndexError:
            temp_index_adjustment = (i+index_adjustmnet)-len(alph)-1
            non_coded_text[i] = alph[temp_index_adjustment]

print(non_coded_text)
