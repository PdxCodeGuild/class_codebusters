

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    dashedStr = ''
    for i in range(len(text)):
        dashedStr += text[i] + '-'
    return dashedStr[:-1].upper()

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    doubleStr = ''
    for i in range(len(word)):
        doubleStr += word[i] + word[i]
    return doubleStr

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    lastLetter = ''
    for i in range(len(word)):
        if word[i] > lastLetter:
            lastLetter = word[i]
    return lastLetter

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    count = 0
    for i in range(len(text)-1):
        if text[i] == 'h' and text[i+1] == 'i':
            count += 1
    return count

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    text = text.lower()
    snakeCase = ''
    for i in range(len(text)):
        if text[i] == ' ':
            snakeCase += '_'
        if text[i] >= 'a' and text[i] <= 'z':
            snakeCase += text[i]
    return snakeCase

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    listText = text.lower().split(' ')
    lowerCase = listText[0].lower()
    i = 1
    while i < len(listText):
        lowerCase += listText[i].title()
        i += 1
    camelCase = ''
    for i in range(len(lowerCase)):
        if (lowerCase[i] >= 'a' and lowerCase [i] <= 'z') or (lowerCase[i] >= 'A' and lowerCase [i] <= 'Z'):
            camelCase += lowerCase[i]
    return camelCase



def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    altCase = ''
    for i in range(len(text)):
        if i % 2 == 0:
            altCase += text[i].upper()
        else:
            altCase += text[i].lower()
    return altCase


def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
