'''
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
'''

# get dollar amount from user, convert to float
amount = float((input('Enter a dollar amount: ')))

# value in pennies, convert to int
in_pennies = int(amount * 100)

# break into each coin, highest to lowest.
# get leftover money after each break

# quarters
quarters = in_pennies // 25
money_left = in_pennies % 25

# dimes
dimes = money_left // 10
money_left = money_left % 10

# nickels
nickels= money_left // 5
money_left = money_left % 5

# pennies
pennies = money_left // 1
money_left = money_left % 1

message = f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies'
print(message)