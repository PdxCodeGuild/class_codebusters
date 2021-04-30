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
#Version 2 Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, 
#separated by commas, then use the .split() function to store each adjective and later use it in your story.
#Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

userInputs = input("Please enter four nouns seperated by commas: ")
def createMadLib(input):
    splitInput = input.split(",")
    return(f"""
    When the {splitInput[random.randint(0,3)]} rises
    I wake up and chase my {splitInput[random.randint(0,3)]}
    I won't regret when the {splitInput[random.randint(0,3)]} sets
    'Cause I live my life like I'm a {splitInput[random.randint(0,3)]}
    """)
print(createMadLib(userInputs))


# Version 3 Make it repeatable. Once you're done prompting the user for words, prompt them for whether 
# they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again 
# until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
'''
message = "yes"
while message != "no":
    userInputs = input("Please enter four nouns seperated by commas: ")
    splitInput = userInputs.split(",")
    reread = "yes"
    while reread != "no":
        print(f"""
        When the {splitInput[random.randint(0,3)]} rises
        I wake up and chase my {splitInput[random.randint(0,3)]}
        I won't regret when the {splitInput[random.randint(0,3)]} sets
        'Cause I live my life like I'm a {splitInput[random.randint(0,3)]}
        """)
        reread = input("Would you like the read the message again? yes or no: ").lower()
    message = input("Would you like play again? yes or no: ").lower()
'''