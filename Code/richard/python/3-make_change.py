coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

userInput = float(input("Enter a dollar amount: ")) * 100

def dollarsToCoins(dollar):
    strOfCoins = ""
    for i in range(len(coins)):
        if dollar / coins[i][1] >= 0:
            numOfCoin = int(dollar // coins[i][1])
            if numOfCoin > 1:
                strOfCoins += f"{numOfCoin} {coins[i][0]}s, "
            elif numOfCoin > 0:
                strOfCoins += f"{numOfCoin} {coins[i][0]}, "
            dollar -= numOfCoin * coins[i][1]
    return strOfCoins[:-2]

print(dollarsToCoins(userInput))