#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Rock paper scissors
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 05/1/21
# 
#----------------------------------------------------#


import random

rungame = True

rps = ['Rock', 'Paper', 'Scissors',] # RPS is an acronym for you know what

while True:

    NPC = random.choice(rps) # this should select a random RPS choice. doing this before the player choice.

    choice = input("""Please type Rock, Paper, or Scissors. You can also request 'Choose for me':    """) # request input
    choice = choice.title() # gotta convert the input to make sure it compares equally to the rps list.

    if choice == "Choose For Me": # this allows you to randomize your choice 
        choice = random.choice(rps)


    error = f"Sorry, looks like {choice} is not valid" # will use this in the event of an error

    print(f"You chose {choice}, the computer chose {NPC}.") # used this to test the functionality of the title()

    # this section will re-arrange the list where the indexs will always be correct based on the input.
    # I.E. rock will always be greater (stronger) than scissors, and lower (weaker) than paper.

    if choice == 'Rock':
        rps = ['Scissors', 'Rock', 'Paper']

    elif choice == 'Paper':
        rps = ['Rock', 'Paper', 'Scissors']

    elif choice == 'Scissors':
        rps = ['Paper', 'Scissors', 'Rock']
    else:
        print(error) # this assumes the input was wrong.
        rungame = False # this will allow us to stop the game, keeping from running the incorrect user input.


    # print( rps[2] > rps[1])  # used this to test the theory that you could convert this whole system into a simple T/F...
    #  
    if rungame == True:
        result = rps.index(choice) > rps.index(NPC) # this bad boy here saved me so much copy/paste. it compares the index value of choice vs NPC

    if not rungame == True: # this keeps us from running a game with bad input.
        print("due to the error game was cancelled.")
    elif choice == NPC:
        print(f"Damn, looks like you tied with {choice}.")
    elif result == True:
        print(f"You win, {choice} beats {NPC}.")
    elif result == False:
        print(f"You lost! {choice} loses to {NPC}.")
    
    while True:
        proceed = input(f'Would you like to proceed with playing another "hand"? type yes or no.:   ').title()
        if proceed == 'No' or proceed == 'Yes':
            break
        else: 
            print(f'Sorry looks like {proceed} was not a valid option')
        
    if proceed == 'No':
        print("Thank you for playing.")
        break
