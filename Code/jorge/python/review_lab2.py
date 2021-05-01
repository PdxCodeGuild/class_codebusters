'''
Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.

Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
'''
import random


def get_words(word_type):
    words = input(f'Enter a(n) {word_type} separated by spaces: ')
    # print(words)
    list_words = words.split(' ')
    random_word = random.choice(list_words)
    return random_word


noun = get_words('noun')
adjective = get_words('adjectives')
verb = get_words('verbs')

print(f'the {adjective} person {verb} the {noun}')
