'''
Unit Converter
Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

ft	mi	m	km
ft	1		0.3048	
mi		1	1609.34	
m	1/0.3048	1/1609.34	1	1/1000
km			1000	1
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
'''
# Version 4

# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# You can think of the values for the conversions as elements in a matrix, where the rows
# will be the units you're converting from, and the columns will be the units you're converting
# to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).
# # Allow the user to also enter the units.
user_unit = input("Enter input unit ('ft', 'mi', 'm', or 'km'): ")
user_unit2 = input("Enter output unit ('ft', 'mi', 'm', or 'km'): ")
user_num = int(
    input(f'Enter number of {user_unit} to convert to {user_unit2}: '))

# Then depending on the units, convert
# the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

#   ft	       mi      	   m         	km
# ft	1	                0.3048
# mi	          1	       1609.34
# m	1/0.3048	1/1609.34	   1	       1/1000
# km			                1000	        1

unit_conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

meter_conversion = {
    'ft': 1/0.3048,
    'mi': 1/1609.34,
    'm': 1,
    'km': 1/1000
}
# Use function for readability within condiional statements


def is_float_num(num):
    # Checks if user input is not a whole number
    if num % 2 != 0:
        return True


converted_unit = 0

for unit in unit_conversion:
    if user_unit == unit:
        converted_unit += user_num * unit_conversion[unit]

for unit in meter_conversion:
    if user_unit2 == unit:
        converted_unit *= meter_conversion[unit]

if is_float_num(converted_unit):
    converted_unit = round(converted_unit, 7)
else:
    # Rounds converted unit to whole numnber
    converted_unit = int(converted_unit)

print(f'{user_num} {user_unit} is {converted_unit} {user_unit2}')

# > what is the distance? 100
# > what are the input units? ft
# > what are the output units? mi
# 100 ft is 0.0189394 mi
