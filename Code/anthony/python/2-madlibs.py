"""
Mad Libs
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result. You can find inspiration here.

Instructions
Search the internet for an example Mad Lib.
Ask the user for each word you'll put in your Mad Lib.
Use string concatenation to combine with user input with other strings to form the Mad Lib.
Display the Mad Lib to the user.
"""

# Version 1
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")

# print(f"The {adjective} person {verb} the {noun}")

"""
Version 2 (optional)
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.

Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
"""




import random
def get_words(word_type):
    words = input(f"Enter a(n) {word_type} seperated by spaces: ")
    # print(words)
    list_words = words.split(' ')
    # random_word = random.randint(0, len(list_words))
    random_word = random.choice(list_words)
    return random_word


noun = get_words("nouns")
adjective = get_words("adjectives")
verb = get_words("verbs")

print(f"The {adjective} person {verb} the {noun}")
