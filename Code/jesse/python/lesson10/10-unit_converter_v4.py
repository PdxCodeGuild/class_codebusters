'''
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

units_in_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

# check if a courrent measurement was entered
def check_measurement(measurement):
    while True:
        if measurement in units_in_meters:
            return measurement
        else:
            measurement = input('\nInvalid entry. Enter "ft," "mi," "m," "km," "yd," or "in": ')

# check if string is int or float was entered and return as such
def check_amount(amount):
    while True:
        if amount.isdigit():
            return int(amount) 
        elif amount.replace('.', '', 1).isdigit():
            return float(amount)
        else:
            amount = input('\nInvalid entry. Enter a number with or without decimals: ')

# get amount of the measurement from user
amount = check_amount(input('\nEnter an amount: '))

# get input measurement from user
input_measurement = check_measurement(input('\nEnter an input measurement (ft, mi, m, km, yd, or in): '))

# get output measurement from user
output_measurement = check_measurement(input('\nEnter an output measurement (ft, mi, m, km, yd, or in): '))

# convert measurment to meters
in_meters = amount * units_in_meters[input_measurement]

# convert meters to output measurement
output = in_meters / units_in_meters[output_measurement]

# round result to 4th decimal place
output = round(output, 4)
if output.is_integer():
    output = int(output)

print(f'\n{amount} {input_measurement} is {output} {output_measurement}\n')