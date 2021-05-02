#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 01
Lab 02 - Mad Libs
Jared Nistler
'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Completed
Version 2: Not Complete - Must Use Functions
Version 3: Under Development

Future Improvements: 
- Utilize Functions to validate user input
- Add more multi-input lists with random placement
- Make user input more user-friendly
'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#
import random

#-----------------------------------------------#
# Input from User
#-----------------------------------------------#

'''
Defines a function that takes in []
and returns []
'''
def get_input():
    return


#Prompt User for First Words and Validates Input
while True:
    house_input = input("Give me two parts of a house (one word each, separated by a comma): ")
    try: 
        # Removes Whitespaces
        house_input = house_input.replace(" ", "")
        # Splits User Input into Two Parts
        house_parts = house_input.split(",")
        # Validates Split and Makes Lower Case
        house_parts[0] = house_parts[0].lower()        
        house_parts[1] = house_parts[1].lower()
        break
    # Catches if user did not submit two words correctly
    except IndexError:
        print("Please enter valid input")

#Prompt User for Remaining Words and Validates Input 
verb_01 = input ("\"I'm tired, I finally [blanked] the old barn out back\": ")
instrument = input ("Name an instrument (plural): ")
verb_02 = input ("\"I'm impressed, Joe [blanks] very well\": ")
object_01 = input ("Name an inanimate object: ")
exclaimation = input ("Give me an angry exclaimation: ")
description = input ("\"My favorite thing about Debra is her [blank]\": ")

#-----------------------------------------------#
# Construct the MADLIB
#-----------------------------------------------#

output = f'''
-----------------------------------------------
Gandalf: [reading] 

"They have taken the {random.choice(house_parts)}... and the second {random.choice(house_parts)}. 
We have {verb_01.lower()} the gates... but cannot hold them for long. 
The ground shakes.
{instrument.capitalize()}... {instrument.lower()}... in the deep.
We cannot get out. A shadow {verb_02.lower()} in the dark.
We cannot get out...
They are coming!"

Pippin: [knocks a {object_01.lower()} into a well]

Gandalf: [slams the book shut]

"{exclaimation.capitalize()}! Throw yourself in next time and rid us of your {description.lower()}!"
-----------------------------------------------
'''
#-----------------------------------------------#
# Print the MADLIB
#-----------------------------------------------#

print (output)

#-----------------------------------------------#
# Original Text for MADLIB
#-----------------------------------------------#
'''
Gandalf: [reading] 

"They have taken the bridge… and the second hall. 
We have barred the gates... but cannot hold them for long. 
The ground shakes.
Drums... drums... in the deep.
We cannot get out. A shadow moves in the dark.
We cannot get out...
They are coming!"

Pippin: [knocks a corpse into a well]

Gandalf: [slams the book shut]

"Fool of a Took! Throw yourself in next time and rid us of your stupidity!"
'''