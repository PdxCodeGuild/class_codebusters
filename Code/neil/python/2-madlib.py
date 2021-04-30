'''
Neil Orbase
28 April 2021
2 - Mad Libs Lab

Mad Libs

Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result. You can find inspiration here.

Instructions

Search the internet for an example Mad Lib.
Ask the user for each word you'll put in your Mad Lib.
Use string concatenation to combine with user input with other strings to form the Mad Lib.
Display the Mad Lib to the user.
Example Run

Give me an antonym for 'data': nonmaterial Tell me an adjective: Bearded Give me a sciency buzzword: half-stack A type of animal (plural): parrots Some Sciency thing: warp drive Another sciency thing: Trilithium crystals Sciency adjective: biochemical

Nonmaterial Scientist Job Description: Seeking a bearded engineer, able to work on half-stack projects with a team of parrots. Key responsibilities:

Extract patterns from non-material
Optimize warp drive
Transform trilithium crystals into biochemical material.
Version 2 (optional)

Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.

Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

Version 3 (optional)

Make it repeatable. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.

'''
# Version 1

# set variables to store user's input for each prompted word
adj1 = input('Give me an adjective: ')
noun1 = input('Give me a noun: ').title()
past_verb1 = input('Give me a verb (past tense): ')
adverb1 = input('Give me an adverb: ')
adj2 = input('Give me another adjective: ')
noun2 = input('Give me another noun: ')
noun3 = input('Give me yet another noun: ')
adj3 = input('Give me yet another adjective: ')
verb = input('Give me a verb: ')
adverb2 = input('Give me another adverb: ')
past_verb2 = input('Give me another verb (past tense): ')
adj4 = input('Give me one last adjective: ')

# concatenate strings to combines user's inputs with other strings
print(f'\n  Today I went to the zoo. I saw a(n) {adj1} {noun1}\njumping up and down in its tree. He {past_verb1}\n{adverb1} through the large tunnel that led to its\n{adj2} {noun2}. I got some peanuts and passed\nthem through the cage to a gigantic gray {noun3}\ntowering above my head. Feeding that animal made\nme hungry. I went to get a {adj3} scoop of ice\ncream. It filled my stomach. Afterwards I had to\n{verb} {adverb2} to catch our bus. When I got\nhome I {past_verb2} my mom for a {adj4} day at the zoo.')
# print mad lib to the user

#--------------------------------------------------------------------------------------------#
'''
Source of mad lib: https://www.it.iitb.ac.in/~vijaya/ssrvm/worksheetscd/getWorksheets.com/Language%20Arts/madlibsdoc.pdf
'''
#--------------------------------------------------------------------------------------------#