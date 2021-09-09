# Make Change
# Let's convert a dollar amount into a number of coins. The input will be the total amount, the 
# output will be the number of quarters, dimes, nickles, and pennies. Always break the total 
# into the highest coin value first, resulting in the fewest amount of coins. First convert the 
# dollar amount (1.36) into the total number of pennies (136), then use floor division //, which 
# throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
# Version 2 (optional)
# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom 
# coins.

coins = [
    ('penny','pennies', 1),
    ('quarter','quarters', 25),
    ('half-dollar','half-dollars', 50),
    ('nickel','nickels', 5),
    ('dime','dimes', 10)
]
#sort coins by value
coins.sort(key=lambda x: x[2], reverse=True)
#Get input from user convert it to a float and multiply by 100
userInput = float(input("Enter a dollar amount: $")) * 100

def dollarsToCoins(dollar):
    strOfCoins = ""
    for i in range(len(coins)):
        if dollar / coins[i][2] >= 0:
            numOfCoin = int(dollar // coins[i][2])
            if numOfCoin > 1:
                strOfCoins += f"{numOfCoin} {coins[i][1]}, "
            elif numOfCoin > 0:
                strOfCoins += f"{numOfCoin} {coins[i][0]}, "
            dollar -= numOfCoin * coins[i][2]
    return strOfCoins[:-2]

print(dollarsToCoins(userInput))

