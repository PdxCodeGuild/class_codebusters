#rock paper scissors 

#import random module
import random

#playing options
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
computer_options = [rock, paper, scissors,]

#REPL
play = 'y'
while play == 'y':
#player choice
    player_choice = input('rock, paper, or scissors: ')

#computer choice

    computer_choice = random.choice(computer_options)

#show round selections
    print(player_choice)
    print(computer_choice)

#game options 
    if player_choice == 'rock' and computer_choice == 'scissors':
        print('player is the winner!')
        
    elif player_choice == 'rock' and computer_choice == 'rock':
        print('tie game')
        
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('computer is the winner!')
        
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('player is the winner!') 
        
    elif player_choice == 'scissors' and computer_choice == 'scissors':
        print('tie game')
        
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('computer is the winner!')
        
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('player is the winner')
        
    elif player_choice == 'paper' and computer_choice == 'paper':
        print('tie game')
        
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('computer is the winner!')
        
    else:
        print('invalid selection please try again.')

#REPL
    play = input('play again y/n?: ')

