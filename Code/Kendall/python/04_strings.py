# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter
import string


def loud_text(text):
    word = '-'.join(list(text))
    return word.upper()


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text(
        'this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'


# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    return ''.join([char * 2 for char in word])


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string


def count_letter(letter, word):
    return word.count(letter)


def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter(
        'p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    latest = []
    for char in word:
        latest.append(ord(char))

    return chr(max(latest))


def test_latest_letter():
    assert latest_letter(
        'pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    return text.count('hi')


def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    word = text.strip(string.punctuation)
    word2 = word.replace(' ', '_')
    return word2.lower()


def test_snake_case():
    assert snake_case('Hello World!') == 'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).


def camel_case(text):
    phrase = text.strip(string.punctuation)
    new_phrase = phrase.title()
    words = new_phrase.split(' ')
    first = [words[0].lower()]
    return ''.join(first + words[1:])


def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

# Alternating Case
# Write a function that converts text to alternating case.


def alternating_case(text):
    new_text = ""
    for idx in range(len(text)):
        if idx % 2 == 0:
            new_text = new_text + text[idx].upper()
        else:
            new_text = new_text + text[idx].lower()

    return new_text


def test_alternating_case():
    assert alternating_case('Hello World!') == 'HeLlO WoRlD!'
    assert alternating_case(
        'This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'
