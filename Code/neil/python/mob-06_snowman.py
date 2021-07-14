'''
Code Busters
Mob Lab 06:
Jared, Jorge, Neil, Richard, and Steve

Snowman

Let's write a program to play a game of Snowman! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.

Part 1

Loading the Words

Let's load in words from a text file. One has been provided here. Or you can navigate to 1 Python > 10 Dictionaries > words.txt. Copy the words from this file, create your own words.txt and paste in the words. Next we can load our file into python with the following:

with open('words.txt', 'r') as file:
    text = file.read()
print(text)
Part 1

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

_ _ _ _ _ _ _ _ _
Guesses remaining: 10
Guess a letter: a
2 a's found

_ a _ _ _ _ a _ _
Guesses remaining: 10
Guess a letter: k
0 k's found

_ a _ _ _ _ a _ _
Guesses remaining: 9
Guess a letter:
Part 2

Keep track of the letters the user has already guessed. If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.

_ _ _ _ _ _ _ _ _
Guesses remaining: 10
Already guessed:
Guess a letter: a
2 a's found

_ a _ _ _ _ a _ _
Guesses remaining: 10
Already guessed: a
Guess a letter: a
You've already guessed that
Part 3

Allow the user to user to guess the whole word- if they enter more than one letter check if the string entered matches the secret word, and if so, they win!

Part 4

We can use the following ASCII art (inspired by this code golf) to show the user how many wrong guesses they've made. Hint: use the number of incorrect guesses as an index into this list.

'''

import random

# Part 0

# with open('words.txt', 'r') as file:
#     text = file.read()
# print(text)

# Part 1

# with open('words.txt', 'r') as file:
#     text = file.read()

# text_list = text.split('\n')

# word = random.choice(text_list)

# game_board = []

# for i in range(len(word)):
#     game_board.append('_')

# guess_remaining = 10

# print(word)

# while guess_remaining > 0:
#     print(''.join(game_board))
#     print(f'Guesses remaining: {guess_remaining}')

#     letter_count = 0

#     guess_letter = input('Guess a letter: ')

#     for i in range(len(word)):
#         if guess_letter == word[i]:
#             game_board[i] = guess_letter
#             letter_count += 1

#     board_check = ''.join(game_board)

#     if board_check == word:
#         print('You guessed it -- Congratulations!')
#         break

#     print(f'{letter_count} {guess_letter}\'s found.')

#     guess_remaining -= 1

# Part 2

# with open('words.txt', 'r') as file:
#     text = file.read()

# text_list = text.split('\n')

# word = random.choice(text_list)

# game_board = []

# for i in range(len(word)):
#     game_board.append('_')

# guess_remaining = 10
# guess_list = []
# print(word)

# while guess_remaining > 0:
#     print(''.join(game_board))
#     print(f'Guesses remaining: {guess_remaining}')

#     letter_count = 0

#     guess_letter = input('Guess a letter: ')

#     if guess_letter not in guess_list:
#         guess_list.append(guess_letter)

#         for i in range(len(word)):
#             if guess_letter == word[i]:
#                 game_board[i] = guess_letter
#                 letter_count += 1

#         board_check = ''.join(game_board)

#         if board_check == word:
#             print('You guessed it -- Congratulations!')
#             break

#         print(f'{letter_count} {guess_letter}\'s found.')

#         guess_remaining -= 1

#     else:
#         print("You've already guessed that!")

# Part 3

# with open('words.txt', 'r') as file:
#     text = file.read()

# text_list = text.split('\n')

# word = random.choice(text_list)

# game_board = []

# for i in range(len(word)):
#     game_board.append('_')

# guess_remaining = 10
# guess_list = []
# print(word)

# while guess_remaining > 0:
#     print(''.join(game_board))
#     print(f'Guesses remaining: {guess_remaining}')

#     letter_count = 0

#     guess_letter = input('Guess a letter: ')

#     if len(guess_letter) > 1:
#         if guess_letter == word:
#             print('Congratulations!')
#             break

#     if guess_letter not in guess_list:
#         guess_list.append(guess_letter)

#         for i in range(len(word)):
#             if guess_letter == word[i]:
#                 game_board[i] = guess_letter
#                 letter_count += 1

#         board_check = ''.join(game_board)

#         if board_check == word:
#             print('You guessed it -- Congratulations!')
#             break

#         if len(guess_letter) > 1:
#             print("You didn't guess the right word. Sucka =P . Try again.")

#         else:
#             print(f'{letter_count} {guess_letter}\'s found.')

#         guess_remaining -= 1

#     else:
#         print("You've already guessed that!")

# Part 4
# snowman_pics = [r'''


#  (   )
# ''', r'''


#  (   )
#  (   )
# ''', r'''

#  (   )
#  (   )
#  (   )
# ''', r'''

#  (   )
#  (   )
#  ( : )
# ''', r'''

#  (   )
#  ( : )
#  ( : )
# ''', r'''

#  ( . )
#  ( : )
#  ( : )
# ''', r'''
#  _===_
#  ( . )
#  ( : )
#  ( : )
# ''', r'''
#  _===_
#  ( .O)
#  ( : )
#  ( : )
# ''', r'''
#  _===_
#  (-.O)
#  ( : )
#  ( : )
# ''', r'''
#  _===_
#  (-.O)
# <( : )
#  ( : )
# ''', r'''
#  _===_
#  (-.O)
# <( : )\
#  ( : )
# ''']

# with open('words.txt', 'r') as file:
#     text = file.read()

# text_list = text.split('\n')

# word = random.choice(text_list)

# game_board = []

# for i in range(len(word)):
#     game_board.append('_')

# guess_remaining = 10
# guess_list = []
# print(word) # For testing purposes

# while guess_remaining >= 0:
#     print(''.join(game_board))
#     print(f'Guesses remaining: {guess_remaining}')
#     print(snowman_pics[10-guess_remaining])

#     if guess_remaining == 0:
#         print('GAME OVER. You lost. - Frosty')
#         break

#     letter_count = 0

#     guess_letter = input('Guess a letter: ')

#     if len(guess_letter) > 1:
#         if guess_letter == word:
#             print('Congratulations!')
#             break

#     if guess_letter not in guess_list:
#         guess_list.append(guess_letter)

#         for i in range(len(word)):
#             if guess_letter == word[i]:
#                 game_board[i] = guess_letter
#                 letter_count += 1

#         board_check = ''.join(game_board)

#         if board_check == word:
#             print('You guessed it -- Congratulations!')
#             break

#         if len(guess_letter) > 1:
#             print("You didn't guess the right word. Sucka =P . Try again.")

#         else:
#             print(f'{letter_count} {guess_letter}\'s found.')

#         guess_remaining -= 1

#     else:
#         print("You've already guessed that!")

# Extra CRUDit

snowman_pics = [r'''



 (   )
''', r'''


 (   )
 (   )
''', r'''

 (   )
 (   )
 (   )
''', r'''

 (   )
 (   )
 ( : )
''', r'''

 (   )
 ( : )
 ( : )
''', r'''

 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( .O)
 ( : )
 ( : )
''', r'''
 _===_
 (-.O)
 ( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )\
 ( : )
''']

with open('words.txt', 'r') as file:
    text = file.read()

text_list = text.split('\n')

word = ''

while True:

    word_length = input('How many letters? ')
    word_length_list = []

    for i in text_list:
        if len(i) == int(word_length):
            word_length_list.append(i)

    if word_length_list:
        word = random.choice(word_length_list)
        break

game_board = []

for i in range(len(word)):
    game_board.append('_')

guess_remaining = 10
guess_list = []
print(word)  # For testing purposes

while guess_remaining >= 0:
    print(''.join(game_board))
    print(f'Guesses remaining: {guess_remaining}')
    print(snowman_pics[10-guess_remaining])

    if guess_remaining == 0:
        print('GAME OVER. You lost. - Frosty')
        break

    letter_count = 0

    guess_letter = input('Guess a letter: ')

    if len(guess_letter) > 1:
        if guess_letter == word:
            print('Congratulations!')
            break

    if guess_letter not in guess_list:
        guess_list.append(guess_letter)

        for i in range(len(word)):
            if guess_letter == word[i]:
                game_board[i] = guess_letter
                letter_count += 1

        board_check = ''.join(game_board)

        if board_check == word:
            print('You guessed it -- Congratulations!')
            break

        if len(guess_letter) > 1:
            print("You didn't guess the right word. Sucka =P . Try again.")

        else:
            print(f'{letter_count} {guess_letter}\'s found.')

        guess_remaining -= 1

    else:
        print("You've already guessed that!")
