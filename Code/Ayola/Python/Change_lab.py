#Let's convert a dollar amount into a number of coins. 
# The input will be the total amount, the output will be the 
# number of quarters, dimes, nickles, and pennies.
#  Always break the total into the highest coin value first, 
# resulting in the fewest amount of coins. 
# First convert the dollar amount (1.36) into the total number of
#  pennies (136), then use floor division //, which throws away 
# the remainder. 10/3 is 3.333333, 10//3 is 3.

#1.36 = 136


from typing import Counter


# def num_of_coins(money):
#     change = [25, 10, 5, 1]  #will convert to cents later (instructor advise)
#     count = 0
#     for coin in change:
#         while money >= coin:
#             money = money - coin 
#             count = count + 1     #add 1 coin

#     return count

# print (num_of_coins(136)) #7 coins
#Given value is $1.36 but will use 136 f
penny = 1
nickel = 5
dime = 10
quarter = 25

n = 0
d = 0
q = 0
p = 0
x = 136     #given value $1.36
x = int(x)


if x >= 25:
    q = x / quarter
    x %= quarter

if x >= 10:
    d = x / dime
    x %= dime
    
if x >= 5:
    n = x / nickel
    x %= nickel

if  x > 0:
    p = x / penny
    x = 0

print ("The coins are %i quarter(s), %i dime(s), %i nickel(s) and %i penny(s))." %(q , d, n, p)) #The coins are 5 quarter(s), 1 dime(s), 0 nickel(s) and 1 penny(s))

