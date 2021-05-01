'''
Let's convert a dollar amount into a number of coins. The input will be the total amount,
the output will be the number of quarters, dimes, nickles, and pennies.
Always break the total into the highest coin value first, resulting in the fewest amount of coins.
First convert the dollar amount (1.36) into the total number of pennies (136), 
then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Version 2 (optional)

Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.
'''

# create a list of tuples with the coins and amounts
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]


# write a def to get amount input and calculate the results
def make_change():
    while True:
        amnt = input('Enter a dollar amount: ')
        try:
            amnt = float(amnt)
            break
        except ValueError:
            print('Invalid entry')

    pennies = amnt * 100
    for coin in coins:
        amnt = pennies / 100
        chnge = coin[1]
        c = pennies // int(chnge)
        pennies -= c * chnge
        print(f'${amnt:.2f} is {int(c)} {coin[0]}')


make_change()
