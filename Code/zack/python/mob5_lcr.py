'''
LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing
it ourselves.
Each player begins with 3 chips. Players take turns rolling three six-sided dice, 
each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. 
For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. 
A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips 
is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, 
they pass the dice on their turn, but may receive chips from others and take their next turn accordingly. 
The winner is the last player with chips left, and wins the center pot.

When the program starts, it should ask for the names of the players, until the user enters 'done'. 
Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again. 
We can represent the players as a list of dictionaries with each dictionary containing two key-value pairs: 
player's name and the number of chips they have, e.g. {'name': 'Billy', 'chips': 3}.
'''

# imports
import random
pot = 0
# functions
def dice_roll(n):
    result = []
    sides = ['L', 'C', 'R', 'dot', 'dot', 'dot']
    counter = 0
    while counter < n:
        roll = random.choice(sides)
        result.append(roll)
        counter += 1
    return result
        
def pass_chips(i,rolls):
    add_pot = 0
    for roll in rolls:
        if roll == 'L':
            player_stats[i]['chips'] -= 1 
            player_stats[i-1]['chips'] += 1
        elif roll == 'C':
            player_stats[i]['chips'] -= 1
            add_pot += 1
        elif roll == 'R':
            player_stats[i]['chips'] -= 1 
            if player_stats[i] == player_stats[-1]:
                player_stats[0]['chips'] += 1
            else:
                player_stats[i+1]['chips'] += 1
        else:
            continue
    return add_pot
    
def game_round(game_pot):
    local_pot = game_pot   
    input('Press any key to play a round!') # round 1 fight  
    for i in range(len(player_stats)):
        if player_stats[i]['chips'] >= 3:
            results = dice_roll(3)
            print(player_stats[i]['player_name'])
            print(results)
            local_pot += pass_chips(i, results)
            print(player_stats)
            print(local_pot)
        elif player_stats[i]['chips'] == 2:
            results = dice_roll(2)
            print(player_stats[i]['player_name'])
            print(results)
            local_pot += pass_chips(i, results)
            print(player_stats)
            print(local_pot)
        elif player_stats[i]['chips'] == 1:
            results = dice_roll(1)
            print(player_stats[i]['player_name'])
            print(results)
            local_pot += pass_chips(i, results)
            print(player_stats)
            print(local_pot)
        else:
            continue
    return local_pot

def the_game():
    game_pot = 0
    winner = False
    while not winner:
        game_pot = game_round(game_pot) 
        for i in range(len(player_stats)):
            if player_stats[i]['chips'] + game_pot == total_chips:
                print(f"{player_stats[i]['player_name']}, is the winner")   
                winner = True
# player
player_stats = []

while True:
    name = input("playername: ")
    if name == 'done':
        break
    else:
        player_stats.append({'player_name': name, 'chips': 3,})
print(player_stats)

total_chips = len(player_stats) * 3

# the game
the_game()


# Left function
# if dice_roll == 'L':
# C = pot = winner winner chicken dinner

#     
# R = i+1



# tests
# print(dice_roll(3))
# pass_chips(0,['L', 'R', 'dot', 'C'])
# print(player_stats)
# print(pot)
