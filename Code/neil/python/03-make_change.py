'''

Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the
output will be the number of quarters, dimes, nickles, and pennies. Always break the total into
the highest coin value first, resulting in the fewest amount of coins. First convert the dollar amount (1.36)
into the total number of pennies (136), then use floor division //, which throws away the remainder. 10/3 is
3.333333, 10//3 is 3.

Output Examples:

Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny

Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies

Version 2 (optional)

Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

'''

dollar_amount = input('Enter dollar amount: ')
dollar_amount = float(dollar_amount)
total_pennies = dollar_amount * 100

# MAKE SURE TO DEDUCT!!!!!

quarters = total_pennies // 25
dimes = total_pennies // 10
nickels = total_pennies // 5
pennies = total_pennies // 1
coins = 0

# quarter_output =
# dime_output =
# nickels_output =
# penny_output =
# # message = ''

while coins <= total_pennies:
    if quarters == 0:
        continue  # check if only 1
    elif quarters == 1:
        coins += (quarters * 25)
        total_pennies -= coins
        quarter_output = f'{quarters} quarter,'
    else:
        coins += (quarters * 25)
        total_pennies -= coins
        quarter_output = f'{quarters} quarters,'

    if dimes == 0:
        continue
    elif dimes == 1:
        coins += (dimes * 10)
        total_pennies -= coins
        dime_output = f'{dimes} dime,'
    else:
        coins += (dimes * 10)
        total_pennies -= coins
        dime_output = f'{dimes} dimes,'

    if nickels == 0:
        continue
    elif nickels == 1:
        coins += (nickels * 10)
        total_pennies -= coins
        nickels_output = f'{nickels} nickel'
    else:
        coins += (nickels * 10)
        total_pennies -= coins
        nickels_output = f'{nickels} nickels,'

    if pennies == 0:
        continue
    elif pennies == 1:
        coins += (pennies * 10)
        total_pennies -= coins
        pennies_output = f'{pennies} penny'
    else:
        coins += (pennies * 10)
        total_pennies -= coins
        pennies_output = f'{pennies} pennies'


message = ''
# 4 == True
# 4
if quarter_output:
    message += f'{quarter_output} '

if dime_output:
    message += f'{dime_output} '

if nickels_output:
    message += f'{nickels_output} '

if pennies_output:
    message += f'{pennies_output}'

print(message)
