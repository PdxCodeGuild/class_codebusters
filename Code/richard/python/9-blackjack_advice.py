# Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking 
# the player for cards. First, ask the user for three playing cards 
# (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their 
# number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following 
# rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

one = input("What's your first card? ").upper()
two = input("What's your second card? ").upper()
three = input("What's your third card? ").upper()

def adviseUser(one,two,three):
    sum = 0
    cardList = [one,two,three]
    for i in range(len(cardList)):
        if cardList[i] == 'A':
            sum += 1
        elif cardList[i] in ['J','Q','K']:
            sum += 10
        else:
            sum += int(cardList[i])
    if sum > 21:
        return f"{sum} Already Busted!"
    elif sum == 21:
        return f"{sum} Blackjack!"
    elif sum >= 17:
        return f"{sum} Stay"
    else:
        return f"{sum} Hit"

print(adviseUser(one,two,three))