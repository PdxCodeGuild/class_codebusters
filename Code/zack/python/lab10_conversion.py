"""
V1
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output.
"""
user_input = input('What is the distance in feet? ')
user_input = float(user_input)
user_output = user_input * 0.3048

print(f'{user_input} feet is {user_output} meters.')


"""
V2 and V3
Allow the user to also enter the units. 
Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, kilometers, yards, and inches.
"""

distance = input('What is the distance? ')
distance = float(distance)
print('units of measurement are ft, mi, m, km, yd, and in')
units = input('What are the units? ')

while True:
    if units == 'ft':
        output = distance * .3048
        break
    elif units == 'mi':
        output = distance * 1609.34
        break
    elif units == 'm':
        output = distance
        break
    elif units == 'km':
        output = distance * 1000
        break
    elif units == 'yd':
        output = distance * .9144
        break
    elif units == 'in':
        output = distance * .0254
        break
    else:
        print('invalid unit of measurement please try again')
        units = input('What are the units? ')
print(f"{distance} {units} is {output} meters.")




"""
V4
Now we'll ask the user for the distance, the starting units, and the units to convert to.
You can think of the values for the conversions as elements in a matrix, 
where the rows will be the units you're converting from, and the columns will be the units you're converting to. 
Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).
But instead of filling out that matrix, and checking for each pair of units 
(if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, 
then convert the distance in meters to any other unit.
Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. 
So first convert from the input units to meters, then convert from meters to the output units.
"""

travel = input('What is the distance? ')
travel = float(travel)
print('units of measurement are ft, mi, m, and, km')
unit_in = input('What are the input units? ')
unit_out = input('What are the output units? ')


def in_convert(unit, distance):    
    if unit == 'ft':
        output = distance * .3048
    elif unit == 'mi':
        output = distance * 1609.34
    elif unit == 'm':
        output = distance
    elif unit == 'km':
        output = distance * 1000
    elif unit == 'yd':
        output = distance * .9144
    elif unit == 'in':
        output = distance * .0254
    else:
        print('invalid unit of measurement please try again')
    return output

def out_convert(unit, distance):
    if unit == 'ft':
        final = distance / .3048
    elif unit == 'mi':
        final = distance / 1609.34
    elif unit == 'm':
        final = distance
    elif unit == 'km':
        final = distance / 1000 
    elif unit == 'yd':
        final = distance / .9144
    elif unit == 'in':
        final = distance / .0254
    return final

to_meters = in_convert(unit_in, travel)
print(to_meters)
from_meters = out_convert(unit_out, to_meters)

print(f"{travel} {unit_in} is {from_meters} {unit_out}")






