'''
Instructions
    Search the internet for an example Mad Lib.
    Ask the user for each word you'll put in your Mad Lib.
    Use string concatenation to combine with user input with other strings to form the Mad Lib.
    Display the Mad Lib to the user.

The [Word Not Submitted] Dragon is the [Word Not Submitted] Dragon of all. It has [Word Not Submitted] [Word Not Submitted], and a [Word Not Submitted] shaped like a [Word Not Submitted]. It loves to eat [Word Not Submitted], although it will feast on nearly anything. It is [Word Not Submitted] and [Word Not Submitted]. You must be [Word Not Submitted] around it, or you may end up as it`s meal!

'''

# Get user input for each word
color = input('Enter a color: ')
superlative = input('Enter a superlative (ending in "est"): ')
adjective1 = input('Enter an adjective:')
body_part1 = input('Enter a body part (plural): ')
body_part2 = input('Enter another body part (singlular): ')
noun = input('Enter a noun: ')
animal = input('Enter an animal (plural): ')
adjective2 = input('Enter another adjective: ')
adjective3 = input('Enter a third adjective: ')
adjective4 = input('Enter a fourth adjective: ')

# Concatenate with the rest of the mad lib
mad_lib = f'''
The {color} Dragon is the {superlative} Dragon of all. It has {adjective1} {body_part1}, and a {body_part2} shaped like a {noun}. It loves to eat {animal}, although it will feast on nearly anything. It is {adjective2} and {adjective3}. You must be {adjective4} around it, or you may end up as it`s meal!
'''

# Display the mad lib
print(mad_lib)
