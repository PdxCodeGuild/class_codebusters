# LCR Simulator
# LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.
import random
from matplotlib import pyplot as plt

# Each player begins with 3 chips. Players take turns rolling three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

# If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left, and wins the center pot.

# When the program starts, it should ask for the names of the players, until the user enters 'done'.
# Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
# We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.


dice = ['l', 'c', 'r', '.', '.', '.']
player_list = []
pot = 0
rounds = 0
players = ["Ayola", "Calen", "Richard", "Neil", "Anthony"]


# while True:
#     name = input('Enter a player name: ').title()
#     if name == 'Done':
#         break
#     player_list.append({
#         'name': name,
#         'chips': 3,
#         'history': [3]
#     })

for player in players:
    player_list.append({
        'name': player,
        'chips': 3,
        'history': [3]
    })

# trying to run 3 instances
# have to go through each player
# if chips >= 3
# can do 3 lines of random choice
# list comp and loops
count = 0

while count != 1:
    rounds += 1
    count = 0
    if pot == 3 * len(player_list):
        break
    for i in range(len(player_list)):
        dice_result = []
        for x in range(min(player_list[i]['chips'], 3)):
            dice_result.append(random.choice(dice))

        for result in dice_result:
            if result == 'l':
                player_list[i]['chips'] -= 1
                player_list[i - 1]['chips'] += 1

            elif result == 'c':
                player_list[i]['chips'] -= 1
                pot += 1

            elif result == 'r':
                if i == len(player_list) - 1:
                    player_list[i]['chips'] -= 1
                    player_list[0]['chips'] += 1

                else:
                    player_list[i]['chips'] -= 1
                    player_list[i + 1]['chips'] += 1
        player_list[i]['history'].append(player_list[i]['chips'])

    # print(player_list)

    # identify if there`s only one player left with chips
    for i in player_list:
        # print(i['chips'])
        if i['chips'] > 0:
            count += 1


for player in player_list:
    if player['chips'] > 0:
        player['history'].append(player['chips'] + pot)
        print(
            f"Congratulations {player['name']} you won {pot + player['chips']} chips. ")
    else:
        player['history'].append(0)
    history = player['history']
    plt.plot(list(range(len(history))), history, label=player['name'])


plt.legend()
plt.show()
