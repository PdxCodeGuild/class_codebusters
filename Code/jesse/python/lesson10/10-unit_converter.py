'''
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''

# check if string is int and return as either int or float
def check_int(num):
    try:
        number = int(num)
        return number
    except:
        number = float(num)
        return number

# get number of feet from user
feet = input('Enter number of feet: ')
feet = check_int(feet)

units_in_meters = {
    'feet': 0.3048
}

# convert feet to meters
in_meters = feet * units_in_meters['feet']

# round result to 4th decimal place
in_meters = round(in_meters, 4)

print(f'{feet} ft is {in_meters} m')