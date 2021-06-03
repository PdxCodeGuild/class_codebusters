'''
Unit Converter
Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
'''
# Version 3

# Add support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m

# Allow the user to also enter the units.
user_unit = input("Enter desired unit ('ft', 'in', 'mi', 'km', or 'yd'): ")
user_num = int(input(f'Enter number of {user_unit} to convert to meters: '))

# Then depending on the units, convert
# the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
unit_conversion = {
    'ft': 0.3048,
    'in': 0.0254,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144
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

elif user_unit == 'in':
    converted_unit += user_num * unit_conversion['in']

elif user_unit == 'km':
    converted_unit += user_num * unit_conversion['km']

elif user_unit == 'mi':
    converted_unit += user_num * unit_conversion['mi']
    if is_float_num(converted_unit):
        converted_unit = round(converted_unit, 2)
    else:
        converted_unit = round(converted_unit)

elif user_unit == 'yd':
    converted_unit += user_num * unit_conversion['yd']

else:
    converted_unit += user_num * unit_conversion['m']

print(f'{user_num} {user_unit} is {converted_unit} m')
