'''
    Search the internet for an example Mad Lib.
    Ask the user for each word you'll put in your Mad Lib.
    Use string concatenation to combine with user input with other strings to form the Mad Lib.
    Display the Mad Lib to the user.
'''

# get user input
noun1 = input('Enter a person, place, or thing: ')
verb1 = input('Enter a verb: ')
noun2 = input('Enter another person, place, or thing: ')
adj1 = input('Enter an adjective: ')
when = input('Enter a period, example; yesterday, next year, a week ago, now: ')
verb2 = input('Enter another verb: ')

# create madlib
madlib = when.capitalize() + ' is the time for all ' + adj1 + ' ' + noun1 + \
    ' to ' + verb1 + ' to the ' + verb2 + ' of their ' + noun2 + '!'

# display output
print('\n', madlib)
