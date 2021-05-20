'''
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be 
the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, 
resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of 
pennies (136), then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
'''

# Get input
amount = float(input("Enter a dollar amount: "))

# Convert to pennies
cents = amount * 100

# quarters
quarter = int(cents // 25)
cents = cents % 25

# dimes
dime = int(cents // 10)
cents = cents % 10

# nickels
nickel = int(cents // 5)
cents = cents % 5

# Pennies left
penny = int(cents)

# Print converted amounts
print(f'{quarter} Quarters {dime} Dimes {nickel} Nickels and {penny} pennies.')
