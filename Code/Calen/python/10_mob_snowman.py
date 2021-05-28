
with open('words.txt', 'r') as file:
    text = file.read()


word = 'testing'
guesses = 10
guessed_words = []
correct_guesses = []
snowman_art = [r'''



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
''',r'''
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

print('*'*50)
print(f'Welcome to the snowman game, you have {guesses} guesses remaining before it\'s game over\n\n what is your first guess?  ')

while guesses > 0: 

    print('*'*50)
    snowman = []
    for letter in word:
        if letter in correct_guesses:
            snowman.append(letter+' ')
        else:
            snowman.append('_ ')
    
    if '_ ' not in snowman:
        break

    print(snowman_art[len(guessed_words)])
    print(''.join(snowman))
    guess = input(f'').lower()

    if guess == word:
        print('Wow! You guessed the word!')
    
    elif len(guess) == 0:
        print('You need to enter a letter to guess')
    
    elif len(guess) > 1:
        print(f"You can only guess one letter at a time, not {guess}")
    
    elif guess in guessed_words:
        print(f'You have already guessed {guess}.')
    
    elif guess in list(word):
        print(f'Correct! {guess} was in the secret word {list(word).count(guess)} time(s)')
        correct_guesses.append(guess)
        guesses -= 1

    else:
        print(f'Your guess of {guess} is incorrect.')
        guessed_words.append(guess)
        guesses -= 1
    
if guesses > 0:
    print(f'Congrats! You guessed the secred word of {word}. you had {guesses} remaining guesses.')
else:
    print(f'You have ran out of guesses, the word was {word}.')