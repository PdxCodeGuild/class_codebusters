'''
Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division //, which throws away the remainder. 
10/3 is 3.333333, 10//3 is 3
'''


import math

dollars = float(input("Enter a dollar amount: "))
# convert dollars to cents
cents = (dollars / .01)

quarter_count = cents / 25

floor_quartercount = math.floor(quarter_count)

remaining_balance = (quarter_count - floor_quartercount)

remaining_afterquarters = cents - floor_quartercount * 25
dimes = remaining_afterquarters / 10

floor_dimecount = math.floor(dimes)

penny_count = dimes - floor_dimecount
new_pennies = penny_count * 10

nickle_count = 0


'''
dime_count = remaining_balance / 10
floor_dimecount = math.floor(dime_count)
'''

print(
    f'quarter_count{floor_quartercount}, dime_count {floor_dimecount}, nickle_count{nickle_count}, penny_count{new_pennies}')
