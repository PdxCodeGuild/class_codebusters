# Rot Cipher
# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, 
# find the corresponding character, add it to an output string. Notice that there are 26 letters in the 
# English language, so encryption is the same as decryption.

rotDecipher = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
    }

'''
userInput = input("Please enter a word to encode: ").lower()
def rotCipherString(input):
    encodedWord = ""
    for i in input:
        if i > 'a' and i < 'z':
            encodedWord += rotDecipher[i]
    return encodedWord
print(rotCipherString(userInput))
'''

# Version 2
# Allow the user to input the amount of rotation used in the encryption. (ROTN)
'''
userInput = input("Please enter a word to encode: ").lower()

def rotCipherString(input):
    encodedWord = ""
    for i in input:
        if i > 'a' and i < 'z':
            encodedWord += rotDecipher[i]
    return encodedWord

numRotations = int(input("Please enter the number of times you want to cipher the word: "))

def rotateRotCipher(num, word):
    for i in range(num):
        word = rotCipherString(word)
    return word

print(rotateRotCipher(numRotations, userInput))
'''
# Version 3 (optional)
# Add support for capital letters, numbers, and special characters. These can be handled in two different 
# ways:

# 1. Capital letters can be rotated as well, numbers and special characters can be put directly into the 
# output (e.g. "hello world!" becomes "uryyb jbeyq!").
'''
userInput = input("Please enter a word to encode: ")

def rotCipherString(input):
    encodedWord = ""
    for i in input:
        if i > 'A' and i < 'Z':
            encodedWord += rotDecipher[i.lower()].upper()
        elif i > 'a' and i < 'z':
            encodedWord += rotDecipher[i]
        else:
            encodedWord += i
    return encodedWord

print(rotCipherString(userInput))
'''
# 2. Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
rotDecipherPlus = {
    'a':'n',
    'b':'o',
    'c':'p',
    'd':'q',
    'e':'r',
    'f':'s',
    'g':'t',
    'h':'u',
    'i':'v',
    'j':'w',
    'k':'x',
    'l':'y',
    'm':'z',
    'n':'a',
    'o':'b',
    'p':'c',
    'q':'d',
    'r':'e',
    's':'f',
    't':'g',
    'u':'h',
    'v':'i',
    'w':'j',
    'x':'k',
    'y':'l',
    'z':'m',
    '0':'!',
    '1':'@',
    '2':'#',
    '3':'$',
    '4':'%',
    '5':'^',
    '6':'&',
    '7':'*',
    '8':'(',
    '9':')',
    '!':'0',
    '@':'1',
    '#':'2',
    '$':'3',
    '%':'4',
    '^':'5',
    '&':'6',
    '*':'7',
    '(':'8',
    ')':'9',
    ' ':'_'
    }
userInput = input("Please enter a word to encode: ")

def rotCipherString(input):
    encodedWord = ""
    for i in input:
        if i > 'A' and i < 'Z':
            encodedWord += rotDecipherPlus[i.lower()].upper()
        else:
            encodedWord += rotDecipherPlus[i]
    return encodedWord

print(rotCipherString(userInput))