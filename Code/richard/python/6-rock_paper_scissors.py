# Rock Paper Scissors
# Let's play rock-paper-scissors with the computer. You may want to try using these emojis 🗿📃✂️ ✊✋✌

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

# rock vs rock (tie)
# rock vs paper
# rock vs scissors
# paper vs rock
# paper vs paper (tie)
# paper vs scissors
# scissors vs rock
# scissors vs paper
# scissors vs scissors (tie)
import random

'''
print("Rock, Paper or Scissors!")
playerChoice = input("Please enter your choice: ").lower()

choices = ['rock','paper','scissor']
compChoice = random.choice(choices)

if playerChoice == compChoice:
    winner = 'Tie'
elif (playerChoice == 'rock' and compChoice == 'scissor') or (playerChoice == 'paper' and compChoice == 'rock') or (playerChoice == 'scissor' and compChoice == 'paper'):
    winner = 'Player'
else:
    winner = 'Computer'

print(f"Player chose {playerChoice} and the computer chose {compChoice}, so the winner is {winner}!")

'''

# Version 2 (optional)
# After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.
'''
playAgain = 'yes'
while playAgain != 'no':
    print("Rock, Paper or Scissors!")
    playerChoice = input("Please enter your choice: ").lower()

    choices = ['rock','paper','scissor']
    compChoice = random.choice(choices)

    if playerChoice == compChoice:
        winner = 'Tie'
    elif (playerChoice == 'rock' and compChoice == 'scissor') or (playerChoice == 'paper' and compChoice == 'rock') or (playerChoice == 'scissor' and compChoice == 'paper'):
        winner = 'Player'
    else:
        winner = 'Computer'

    print(f"Player chose {playerChoice} and the computer chose {compChoice}, so the winner is {winner}!")
    playAgain = input("Would you like to play again? ").lower()
'''
# Version 3 (optional)
# Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-
# Lizard-Spock/

playAgain = 'yes'
while playAgain != 'no':
    print("Rock, Paper, Scissors, Lizard, Spock!")
    playerChoice = input("Please enter your choice: ").lower()

    choices = ['rock','paper','scissor','lizard','spock']
    compChoice = random.choice(choices)

    if playerChoice == compChoice:
        winner = 'Tie'
    elif(
        (playerChoice == 'rock' and (compChoice == 'scissor' or compChoice == 'lizard')) or 
        (playerChoice == 'paper' and (compChoice == 'rock' or compChoice == 'spock')) or 
        (playerChoice == 'scissor' and (compChoice == 'paper' or compChoice == 'lizard')) or
        (playerChoice == 'lizard' and (compChoice == 'paper' or compChoice == 'spock')) or
        (playerChoice == 'spock' and (compChoice == 'scissor' or compChoice == 'rock'))
        ):
        winner = 'Player'
    else:
        winner = 'Computer'

    print(f"Player chose {playerChoice} and the computer chose {compChoice}, so the winner is {winner}!")
    playAgain = input("Would you like to play again? ").lower()