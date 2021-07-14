# copied from https://github.com/PdxCodeGuild/class_codebusters/blob/main/1%20Python/07%20Strings/strings_practice.py
# edited by Calen Ray   


# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

import string

def loud_text(text):
    # lets be real, there is a more simple solution, using a 'sep = '-'' of some kind, but this solution is a bit out of the box and funtional. 
    text = text.upper() # force uppercase
    new_list = [] # create new list to append to 
    for x in text: # turn the string into a list, while adding a hyphen after every 'x'
        new_list.append(x)
        new_list.append('-')
    new_list.pop() # use this to elimite the final hyphen
    text = ''.join(new_list) #turn this b, back into a string
    return text # return it under the guise of the original variable, like indiana jones swiping the totem for a bad of sand.


def test_loud_text():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'
    assert loud_text('WhO eVeR ThReW ThAt, yOuR mOm iS a HoE.') == 'W-H-O- -E-V-E-R- -T-H-R-E-W- -T-H-A-T-,- -Y-O-U-R- -M-O-M- -I-S- -A- -H-O-E-.'

# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    # I suppose I would approach this with the same idea
    new_word_list = []
    for x in word:
        new_word_list.append(x+x)
    word = ''.join(new_word_list)
    return word


def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    #well damn, another one where a for loop is the first thing that comes to mind.
    letter_count = 0
    for x in word:
        if x == letter:
            letter_count += 1
    return letter_count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    # going to move on and come back to this one later.
    word = word.lower()
    alp = string.ascii_lowercase



def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    text_list = [] # this will allow us to address text by index
    hi_count = 0 # use this for our return value
    text= text.lower() # lower case to allow for proper validation of 'hi' vs Hi vs HI vs hI etc.
    for x in text: # covert text into a list
        text_list.append(x)
    list_count = 0 # use this to count the next item in the list
    for y in text_list:
        list_count += 1
        try:
            if y == 'h' and text_list[list_count] == 'i': # now its as simple as scanning for any instance in which an I follows an h. 
                hi_count += 1
        except:
            pass
    return hi_count # and boom, it works. never even tested it. 
            

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    text = text.lower() # convert to lowercase
    text_list = []#create a text list for ease of index and appending.
    punc = []#use this to create a list of punctuation

    for y in string.punctuation: # make a list of punct. (originally used 'if x in string.punctuation', but changed to a list when I was getting errors)
        punc.append(y)

    for x in text: # for each letter in text, check if its in punc list, then check if its a space, if not either, add to text_list
        if x in punc:
            pass
        elif x == ' ':
            text_list.append('_')
        else:
            text_list.append(x)
    text = ''.join(text_list) # convert to string
    return text # return to sender 

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    text = text.lower()
    text_list = []
    loop_counter = 0
    next_letter_cap = False
    for x in text:
        loop_counter += 1
        if x != ' ' and x not in string.punctuation:
            if next_letter_cap == True:
                x = x.upper()
                next_letter_cap = False
            text_list.append(x)
        elif x == ' ':
            next_letter_cap = True
    text = ''.join(text_list)
    return text

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    next_letter_cap = True
    new_text_list = []
    for letter in text:
        if next_letter_cap == True:
            letter = letter.upper()
            new_text_list.append(letter)
            next_letter_cap = False
        else:
            next_letter_cap = True
            new_text_list.append(letter)
    return ''.join(new_text_list)
    
def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'