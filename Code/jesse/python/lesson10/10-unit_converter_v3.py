'''
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
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
            measurement = input('Invalid entry. Enter "ft," "mi," "m," "km," "yd," or "in": ')

# check if string is int or float was entered and return as such
def check_amount(amount):
    while True:
        if amount.isdigit():
            return int(amount) 
        elif amount.replace('.', '', 1).isdigit():
            return float(amount)
        else:
            amount = input('Invalid entry. Enter a number with or without decimals: ')

# get amount of the measurement from user
amount = check_amount(input('Enter an amount: '))

# get measurement from user
measurement = check_measurement(input('Enter a measurement (ft, mi, m, km, yd, or in): '))

# convert measurment to meters
in_meters = amount * units_in_meters[measurement]

# round result to 4th decimal place
in_meters = round(in_meters, 4)
if in_meters.is_integer():
    in_meters = int(in_meters)

print(f'{amount} {measurement} is {in_meters} m')