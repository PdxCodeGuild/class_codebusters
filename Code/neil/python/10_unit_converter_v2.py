'''
Unit Converter
Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

'''
# Version 2

# Allow the user to also enter the units.
user_unit = input("Enter desired unit ('ft', 'm', 'km', or 'mi'): ")
user_num = int(input(f'Enter number of {user_unit} to convert to meters: '))

# Then depending on the units, convert
# the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
unit_conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}
# Use function for readability within condiional statements


def is_float_num(num):
    # Checks if user input is not a whole number
    if num % 2 != 0:
        return True


converted_unit = 0

if user_unit == 'ft':
    converted_unit += user_num * unit_conversion['ft']
    if is_float_num(converted_unit):
        converted_unit = round(converted_unit, 4)
    else:
        # Rounds converted unit to whole numnber
        converted_unit = round(converted_unit)

elif user_unit == 'mi':
    converted_unit += user_num * unit_conversion['mi']
    if is_float_num(converted_unit):
        converted_unit = round(converted_unit, 2)
    else:
        converted_unit = round(converted_unit)

elif user_unit == 'km':
    converted_unit += user_num * unit_conversion['km']

else:
    converted_unit += user_num * unit_conversion['m']

print(f'{user_num} {user_unit} is {converted_unit} m')
