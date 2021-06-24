#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 01
Lab 03 - Make Change
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, 
dimes, nickles, and pennies. Always break the total into the highest coin value 
first, resulting in the fewest amount of coins. First convert the dollar amount 
(1.36) into the total number of pennies (136), then use floor division //, which 
throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: Complete

Future Improvements:

- Fix the output to use natural language

'''

#-----------------------------------------------#
# Create Coins
#-----------------------------------------------#

# Creates coin list in a Tuple
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

#-----------------------------------------------#
# User Input
#-----------------------------------------------#

# Solicit user input
num_input = input("Enter a dollar amount: ")
# Convert input to float
num_input = float(num_input)
# Convert dollar amount to pennies
num_input = num_input * 100
# convert penny amount to int
num_input = int(num_input)

#-----------------------------------------------#
# Break Down Coins
#-----------------------------------------------#

# Create list in which to store results
total_count = []

# Iterate through each coin type
for coin in coins:
    # If there are still pennies to count, count them
    if num_input > 0:
        # Add the number of coins counted to the total count list
        total_count.append([coin[0], num_input//coin[1]])
        # Subtract the number of coins counted from the pennies remaining
        num_input %= coin[1]
    else:
        # If there are no coins left to be cointed, add that to list
        total_count.append([coin[0], 0])

#-----------------------------------------------#
# Print Output
#-----------------------------------------------#

print(f'''
----------------------------
Here are your coins:
----------------------------
''')
for coin in total_count:
    print(f"{coin[0]}: {coin[1]}")