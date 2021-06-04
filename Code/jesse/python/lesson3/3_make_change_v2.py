'''
Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''

# list of coin-value tuples
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

print(coins[0][1])

# get dollar amount from user, convert to float
amount = float((input('Enter a dollar amount: ')))

# value in pennies, convert to int
money_left = int(amount * 100)

# break into each coin, highest to lowest.
# get leftover money after each break

# half-dollars
half_dollars = money_left // coins[0][1]
money_left = money_left % coins[0][1]

# quarters
quarters = money_left // coins[1][1]
money_left = money_left % coins[1][1]

print (quarters)
print (money_left)
# dimes
dimes = money_left // coins[2][1]
money_left = money_left % coins[2][1]

# nickels
nickels= money_left // coins[3][1]
money_left = money_left % coins[3][1]

# pennies
pennies = money_left // coins[4][1]
money_left = money_left % coins[4][1]

message = f'{half_dollars} half-dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies'
print(message)