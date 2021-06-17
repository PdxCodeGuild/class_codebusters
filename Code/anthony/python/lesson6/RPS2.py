"""
    Rock Paper Scissors with NO conditional statements.

"""
import random

choices = ['rock', 'paper', 'scissors']
choice_dict = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

# temp = choice_dict.get('lizard', "Invalid option")

result = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0],
    [2, 2, 2]
]

result_message = {
    -1: "You lost",
    0: "It was a draw",
    1: "You won",
    2: "Invalid option"
}

play_again = {
    "yes": True,
    "no": False
}

running = play_again['yes']
while running:
    user = choice_dict.get(
        input(f"Select one of the following: {choices} ->"), 3)
    computer = random.randint(0, 2)
    code = result[user][computer]
    print(result_message[code])
    running = play_again.get(
        input("Do you want to play again (yes/no)? "), False)
