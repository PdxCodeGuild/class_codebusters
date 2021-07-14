

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

import string


def loud_text(text):
    # text = text.upper()
    # return "-".join(text)
    # text.split()
    return "-".join(text).upper()


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    # letters = ''
    # for i in word:
    #     letters += i * 2
    # return letters

    # return "".join([char*2 for char in word])

    double = []
    letters = list(word)
    for i in letters:
        double.append(i*2)
        # double.append(i)
    return "".join(double)


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string


def count_letter(letter, word):
    # return word.count(letter)
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    # char_list = list(word)
    # char_list.sort()
    # return char_list[-1]

    order = []
    for i in word:
        order.append(ord(i))
    return chr(max(order))


def test_latest_letter():
    assert latest_letter(
        'pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    # return text.count('hi')

    count = 0
    # for i in range(len(text) - 1):
    #     if text[i] == 'h' and text[i + 1] == 'i':
    #         count += 1
    # return count

    for i in range(len(text)):
        if text[i:i+2] == 'hi':
            count += 1
    return count

    # hi_count = 0
    # text = text.lower()
    # list_count = 0
    # for y in text:
    #     list_count += 1

    #     try:
    #         if text[list_count] == "i" and y == 'h':
    #             hi_count += 1
    #     except:
    #         pass

    # return hi_count


count_hi('hihi')


def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2
    assert count_hi('hihih') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).


def snake_case(text):
    # for char in text:
    #     if char in string.punctuation:
    #         text = text.replace(char, '')
    # return text.lower().replace(' ', '_')

    # return text.lower().replace(' ', '_').strip(string.punctuation)
    return text.lower().replace(' ', '_').strip('.!?')


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).


def camel_case(text):
    return text.title().replace(' ', '').strip('.!?').replace(text[0], text[0].lower())


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case
# Write a function that converts text to alternating case.


def alternating_case(text):
    result = ''
    # counter = 1
    # for char in text:
    #     if counter % 2:
    #         result += char.upper()
    #     else:
    #         result += char.lower()
    #     counter += 1
    # return result

    for index, char in enumerate(text):
        if index % 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        result += char
    return result


def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
