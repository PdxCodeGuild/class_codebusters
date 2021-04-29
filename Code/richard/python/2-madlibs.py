# Mad Libs
# Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result. You can find inspiration here.

# Instructions
# Search the internet for an example Mad Lib.
# Ask the user for each word you'll put in your Mad Lib.
# Use string concatenation to combine with user input with other strings to form the Mad Lib.
# Display the Mad Lib to the user.
import random
'''
sun = input("Please enter a noun: ")
dreams = input("Please enter something you would chase: ")
regret = input("Please enter a verb: ")
beast = input("Please enter a type of animal: ")
print(f"""
When the {sun} rises
I wake up and chase my {dreams}
I won't {regret} when the sun sets
'Cause I live my life like I'm a {beast}
""")
'''
# Version 2 Make a functional solution that utilizes lists
userInputs = input("Please enter four nouns seperated by commas: ")
splitInput = userInputs.split(",")
print(f"""
When the {splitInput[random.randint(0,3)]} rises
I wake up and chase my {splitInput[random.randint(0,3)]}
I won't regret when the {splitInput[random.randint(0,3)]} sets
'Cause I live my life like I'm a {splitInput[random.randint(0,3)]}
""")