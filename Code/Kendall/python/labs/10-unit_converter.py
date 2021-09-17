# Created a function for each of the conversions (ft--m, mi--m, km--m, yd--m, in--m)


def feet_meter(distance_ft):
    meters = round((distance_ft * .3048), 4)
    return meters


def yd_meter(distance_yd):
    meters = round(((distance_yd * 3) * .3048), 4)
    return meters


def in_meter(distance_in):
    meters = round(((distance_in / 12) * .3048), 4)
    return meters


def mile_meter(distance_mile):
    meters = round((distance_mile * 1609.34), 4)
    return meters


def km_meter(distance_km):
    meters = round((distance_km * 1000), 4)
    return meters


# Created a dictionary and assigned each function as a value
conversions = {
    'ft': feet_meter,
    'mi': mile_meter,
    'km': km_meter,
    'yd': yd_meter,
    'in': in_meter
}
user = {}

# Assigned the user inputs as values to a separate dictionary with separate keys
user['input_distance'] = float(input('What is the distance? '))
user['output_distance'] = 1
user['final_distance'] = 1
user['input_unit'] = input('What are the input units? ')
user['output_unit'] = input('What are the output units? ')

# Used the conversions dictionary to call the fucntion based on user input and print result
# Convert to meters first
if user['input_unit'] == 'm':
    user['output_distance'] = user['input_distance']

if user['input_unit'] != 'm':
    if user['input_unit'] == 'ft':
        user['output_distance'] = feet_meter(user['input_distance'])
    elif user['input_unit'] == 'yd':
        user['output_distance'] = yd_meter(user['input_distance'])
    elif user['input_unit'] == 'km':
        user['output_distance'] = km_meter(user['input_distance'])
    elif user['input_unit'] == 'mi':
        user['output_distance'] = mile_meter(user['input_distance'])
    elif user['input_unit'] == 'in':
        user['output_distance'] = in_meter(user['input_distance'])


if user['output_unit'] == 'm':
    user['final_distance'] = user['output_distance']

if user['output_unit'] != 'm':
    if user['output_unit'] == 'ft':
        user['final_distance'] = user['output_distance'] * 3.2808
    elif user['output_unit'] == 'yd':
        user['final_distance'] = user['output_distance'] * 1.0936
    elif user['output_unit'] == 'km':
        user['final_distance'] = user['output_distance'] * 1000
    elif user['output_unit'] == 'mi':
        user['final_distance'] = user['output_distance'] * .000621371
    elif user['output_unit'] == 'in':
        user['final_distance'] = user['output_distance'] * 39.3701

else:
    print('You did not enter a valid unit')

#final_distance = conversions[user['output_unit']](user['output_distance'])
print(f'{user["input_distance"]} {user["input_unit"]} is {user["final_distance"]} {user["output_unit"]}')
