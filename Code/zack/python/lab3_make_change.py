#creating a function to return chanfe amount

#imports
import math

# change types
quarter = 25
dime = 10
nickel = 5
penny = 1

# input change amount
first = input('how much money was spent?: ')
# convert change from dollars into cents
first = float(first)
first = first * 100
# ease of use
first = int(first)

# change conversion
def change_filter(first):
    second = first % quarter
    third = second % dime
    fourth = third % nickel
    print(f"{first // quarter} quarters, {second // dime} dimes, {third // nickel} nickels, and {fourth // penny} pennies")

#perform function
change_filter(first)
