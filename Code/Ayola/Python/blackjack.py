card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
               '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10}


print("Card input options: ", "A 2 3 4 5 6 7 8 9 10 J K Q")
while True:
    added_value = 0
    for turn in ['first', 'second', 'third']:
        user_inp = input("What's your " + turn + " card? ")
        while (user_inp not in card_values.keys()):
            print("INVALD CARD!")
            user_inp = input("What's your " + turn + " card? ")

        added_value += card_values[user_inp]
    if added_value < 17:
        print(added_value, "Hit")

    elif (added_value >= 17 and added_value < 21):
        print(added_value, "Stay")

    elif (added_value == 21):
        print(added_value, "BlackJack!")

    else:
        print(added_value, "Already Busted")
