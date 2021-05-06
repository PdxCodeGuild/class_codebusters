import random
user = input("Choose rock, paper, or scissors: ")
computer = ["rock", "paper", "scissors"]
'rock' > "scissors" > 'paper'
choice = random.choice(computer)
print('I chose ' + choice)

if user > choice:
    print('You win')
if choice > user:
    print('I win')
