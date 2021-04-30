'''
Version 3 (optional)
Make it repeatable. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
'''

# import the random module
# Get user input for each word
from random import *
color = input('Enter a color: ')
superlative = input('Enter a superlative (ending in "est"): ')

# get four adjectives from user
adjectives = input('Enter four adjectives, separated by commas: ')

# convert adjectives to list
adjectives = adjectives.split(', ')

# randomize adjectives
shuffle(adjectives)

body_part1 = input('Enter a body part (plural): ')
body_part2 = input('Enter another body part (singlular): ')
noun = input('Enter a noun: ')
animal = input('Enter an animal (plural): ')

# Concatenate with the rest of the mad lib
mad_lib = f'''
The {color} Dragon is the {superlative} Dragon of all.
It has {adjectives[0]} {body_part1}, and a {body_part2}
shaped like a {noun}. It loves to eat {animal},
although it will feast on nearly anything. It is {adjectives[1]}
and {adjectives[2]}. You must be {adjectives[3]} around it, or 
you may end up as it`s meal!
'''

# prompt user if they would like to hear the story again until the answer is "no"
prompt = input('\nData received. Would you like to hear the story? ')
if prompt == 'yes':
    while True:
        print(mad_lib)
        prompt = input('Would you like to hear the story again? ')
        if prompt == 'no':
            print('\nGoodbye!\n')
            break
