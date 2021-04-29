'''
Search the internet for an example Mad Lib.
Ask the user for each word you'll put in your Mad Lib.
Use string concatenation to combine with user input with other strings to form the Mad Lib.
Display the Mad Lib to the user.
'''

# input statement for madlib
Noun1 = input('Enter a noun ')
Noun2 = input('Enter a plural noun ')
Noun3 = input('Enter another noun ')
Place = input('Enter a place ')
Adjective = input('Enter a adjective ')
Noun4 = input('Enter another noun ')

# print statement concatinating the outputs from each input statement
print('Be kind to your Robber-footed ' + Noun1)
print("For a duck may be somebody's " + Noun2)
print('Be kind to your ' + Noun3 + " in " + Place)
print('Where the weather is always ' + Adjective)
print('You may think that this is the ' + Noun4)
print('Well it is.')
