'''
Version 3 (optional)
Make it repeatable. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
'''

# import the random module
from random import *

# Get user input for each word
# convert all answers to lowercase
color = input('Enter a color: ').lower()
superlative = input('Enter a superlative (ending in "est"): ').lower()

# get four adjectives from user
adjectives = input('Enter four adjectives, separated by spaces: ').lower()

# convert adjectives to list
adjectives = adjectives.split(' ')

# randomize adjectives
shuffle(adjectives)

body_part1 = input('Enter a body part (plural): ').lower()
body_part2 = input('Enter another body part (singlular): ').lower()
noun = input('Enter a noun: ').lower()
animal = input('Enter an animal (plural): ').lower()

# Concatenate with the rest of the mad lib
mad_lib = f'''
The {color} Dragon is the {superlative} Dragon of all.
It has {adjectives[0]} {body_part1}, and a {body_part2}
shaped like a {noun}. It loves to eat {animal},
although it will feast on nearly anything. It is {adjectives[1]}
and {adjectives[2]}. You must be {adjectives[3]} around it, or 
you may end up as it`s meal!'''

# prompt user if they would like to hear the story again until the answer is "no"
# convert all user inputs to lowercase
while True:
    prompt = input('\nData received. Would you like to hear the story? ').lower()
    if prompt == 'yes':
        print(mad_lib)

        # ask the user if they would like to hear the story 
        # again until the answer is no, but with a different message than before
        while True:
            prompt = input('\nWould you like to hear the story again? ').lower()
            if prompt == 'yes':
                print(mad_lib)
                continue
            elif prompt == 'no':
                print('\nGoodbye!\n')
                exit()
    elif prompt == 'no':
        print('\nGoodbye!\n')
        break