# Random Emoticon Generator
# Let's generate emoticons by randomly choosing a set of eyes, a nose, 
# and a mouth. Examples of emoticons are :-D =^P and :\. You can view a 
# long list on wikipedia.
# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Use concatenation to combine them and display the emoticon
import random
'''
eyes = [':','=',';','>',]
noses = ['-','']
mouths = [')','D','}','P','O','X',']','(']

def createEmoticon():
    return f"{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}"

print(createEmoticon())
'''
#version 2 Use a while loop to generate 5 emoticons.
'''
eyes = [':','=',';','>',]
noses = ['-','']
mouths = [')','D','}','P','O','X',']','(']

def createEmoticon():
    return f"{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}"
i = 0
while i < 5:
    print(createEmoticon())
    i += 1
'''
#version 3 Randomly generate vertical emoticons like ^_^ (-_-), [*.*]
eyes = ['^','-','*']
cheeks = ['(','[','']
mouths = ['-','.']

def createEmoticon():
    eye = random.choice(eyes)
    mouth = random.choice(mouths)
    leftCheek = random.choice(cheeks)
    
    if leftCheek == '(':
        rightCheek = ')'
    elif leftCheek == '[':
        rightCheek = ']'
    else:
        rightCheek = ''
    return f"{leftCheek}{eye}{mouth}{eye}{rightCheek}"

print(createEmoticon())