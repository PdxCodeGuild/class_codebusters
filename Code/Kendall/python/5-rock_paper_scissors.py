import random

choices = ['rock', 'paper', 'scissors']
cpu_choice = random.choice(choices)
count = 1

user_choice = input('rock, paper or scissors? ')


if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':

    print(f'Opponent chose: {cpu_choice}')

    if user_choice == cpu_choice:
        print('TIE')
    elif user_choice == 'rock' and cpu_choice == 'paper':
        print('YOU LOSE!')
    elif user_choice == 'rock' and cpu_choice == 'scissors':
        print('YOU WIN!')
    elif user_choice == 'paper' and cpu_choice == 'rock':
        print('YOU WIN!')
    elif user_choice == 'paper' and cpu_choice == 'scissors':
        print('YOU LOSE!')
    elif user_choice == 'scissors' and cpu_choice == 'rock':
        print('YOU LOSE!')
    elif user_choice == 'scissors' and cpu_choice == 'paper':
        print('YOU WIN!')
else:
    print("Invalid Entry")
