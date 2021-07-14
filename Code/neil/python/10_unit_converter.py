'''
Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''

# Version 1

# Ask the user for the number of feet
num_in_feet = int(input('Enter number of feet to convert to meters: '))
# Display user input in feet and round the product of user input times 0.3048 by 4 decimal places
print(f'{num_in_feet} ft is {round(num_in_feet * 0.3048, 4)} m')
