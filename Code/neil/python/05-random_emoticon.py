'''

Random Emoticon Generator

Let's generate emoticons by randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\. You can view a long list on wikipedia.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Use concatenation to combine them and display the emoticon
Example output:

:-P
Version 2

Use a while loop to generate 5 emoticons.

Version 3

Randomly generate vertical emoticons like ^_^ (-_-), [*.*]

'''
# Version 1
import random

eyes = [";",  ":", "|", "8", "=", ">:"]
nose = ["L", "O", "o", "*", "-", "^"]
mouths = ["$", "/", "\\", "D", "[", "3"]

# a = random.choice(eyes)
# b = random.choice(nose)
# c = random.choice(mouths)

# print(a + b + c)

# Version 2

i = 0  # iterator

while i in range(5):
    a = random.choice(eyes)  # randomly generate char through each iteration
    b = random.choice(nose)
    c = random.choice(mouths)
    print(a + b + c)
    i += 1
