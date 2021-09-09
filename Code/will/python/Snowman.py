#Calen, Zack, Jesse, David, Kendell

'''
Let's load in words from a text file. One has been provided here.
 Or you can navigate to 1 Python > 10 Dictionaries > words.txt. 
 Copy the words from this file, create your own words.txt and paste in the words. 
 Next we can load our file into python with the following:
'''

'''
Part 1
Show them a list of 'blanks' and ask them for a letter. 
If they guess a letter which is in the word, show the blanks with the letters filled in. 
If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. 
Allow the user 10 tries to guess the letters of the word. If the user can't guess the word in the number of allotted guesses, 
print the word and ask them if they'd like to play again.
Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.


Part 2
Keep track of the letters the user has already guessed. If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.

Part 3 
Allow the user to user to guess the whole word- if they enter more than one letter check if the string entered matches the secret word, and if so, they win!

Part 4 

We can use the following ASCII art (inspired by this code golf) to show the user how many wrong guesses they've made. Hint: use the number of incorrect guesses as an index into this list.
'''

# with open('../../../1 Python/10 Dictionaries/words.txt', 'r') as file:
#     text = file.read()

import random
with open('./words.txt', 'r') as file:
    text = file.read()

wordlist = text.split('\n')
wordlist.remove('')
magicword = random.choice(wordlist)


def blankword(word, guessed=''):
    blank = ''
    for let in word:
        if let in guessed:
            blank += let + ' '
        else:
            blank += '_ '
    return blank


def play_snowman():
    guesses = 10
    prev_guess = []

    print(f"Welcome to the Snowman B*tch {guesses} remaining guesses")

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

    while guesses > 0:
        print(snowman_pics[10-guesses])
        print(blankword(magicword, prev_guess))
        if '_ ' not in blankword(magicword, prev_guess):
            break
        new_guess = input("Enter a letter or guess the word: ").lower()
        if new_guess == magicword:
            print("You smug bastard")
            break
        elif len(new_guess) != 1:
            print("Wrong guess, m'fer")
            guesses -= 1
        elif new_guess in prev_guess:
            print(
                f"Is there an echo in here? You already guessed {new_guess}!")
        elif new_guess in magicword:
            prev_guess.append(new_guess)
            print(
                f"Correct! {new_guess} was in secret word {list(magicword).count(new_guess)} times")
        elif new_guess not in magicword:
            prev_guess.append(new_guess)
            guesses -= 1
            print(f"{new_guess} was whack.\nYou have {guesses} left.")

    if guesses > 0:
        print(
            f"Congrats you guessed the word {magicword}. You had {guesses} remaining guesses.")
        return True
    else:
        print(f"You lose. The word was {magicword}")
        return False


game_again = 'y'
while True:
    if game_again == 'y':
        play_snowman()
    game_again = input("Would you like to play again? y/n ")
    if game_again == 'y':
        continue
    elif game_again == 'n':
        break
    else:
        print("Speak English please.")
