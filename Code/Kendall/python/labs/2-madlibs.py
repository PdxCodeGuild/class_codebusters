"""
Lab 2 - Mad Lib

1. Search the internet for an example Mad Lib.
2. Ask the user for each word you'll put in your Mad Lib.
3. Use string concatenation to combine with user input with other strings to form the Mad Lib.
4. Display the Mad Lib to the user.

"""

# I assigned each input to a separate variable and used those inputted variables in a f string to create a functioning Madlib.
holiday = input('Enter a holiday: ')
noun = input('Enter a noun: ')
place = input('Enter a place: ')
name = input('Enter a name: ')
adjective = input('Enter a adjective: ')
body = input('Enter a body part: ')
verb = input('Enter a verb: ')
adjective2 = input('Enter another adjective: ')
noun2 = input('Enter another noun: ')
food = input('Enter something you eat: ')
noun3 = input('Enter one more noun: ')

# Prints the mad lib with user submitted values
print(f'''\nI can\'t believe it\'s already {holiday}. \nI can\'t wait to put on my {noun} and visit every {place} in the neighborhood. 
This year I\'m going to dress up as {name} with {adjective} {body}. Before I {verb}, I make sure to grab my {adjective2} {noun2} to hold all of my {food}.
Finally, all of my {noun3}s are ready to go! ''')
