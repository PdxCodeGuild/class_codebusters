# Version 1
''' 
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
'''

#input number of feet
user_input = int(input("What is the distance in feet? "))
#print out distance in meters
input_meters = user_input * 0.3048
print(f" {user_input} ft is {input_meters} meters")

# Version 2
'''
Allow the user to also enter the units. 
Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
'''

# input amount
amount = input("What is the distance? ")
# input units
units = input('What are the units? ').lower()

# dict with measures
measures = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000}

# convert distance to meters
converted_amount = float(amount) * measures[units]
int(converted_amount)
print(f"{amount} {units} is {converted_amount} m")


# Version 3
# Add support for yards, and inches.

# input amount
amount = input("What is the distance? ")
# input units
units = input('What are the units? ').lower()

# dict with measures
measures = {'ft': 0.3048, 'mi': 1609.34, 'm': 1,
            'km': 1000, 'yd': 0.9144, 'in': 0.0254}

# convert distance to meters
converted_amount = float(amount) * measures[units]
int(converted_amount)
print(f"{amount} {units} is {converted_amount} m")


# Version 4
'''
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, 
where the rows will be the units you're converting from, and the columns will be the units you're converting to. 
Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), 
we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above.
 So first convert from the input units to meters, then convert from meters to the output units.
'''

# input amount
amount = input("What is the distance? ")
# input units
units = input('What are the input units? ').lower()
# input units to convert to
units_convert = input('What are the output units? ').lower()

# dict with measures
meters = {'ft': 0.3048, 'mi': 1609.34, 'm': 1,
          'km': 1000}
# output_units = {'ft': 0.3048, 'mi': 1609.34, 'm': 1,
#                 'km': 1000}

# convert distance to meters
units_in_meters = float(amount) * meters[units]
# int(units_in_meters)
converted_units = units_in_meters / meters[units_convert]

print(f"{amount} {units} is {converted_units} {units_convert}")
