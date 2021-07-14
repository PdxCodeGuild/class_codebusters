"""
Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.
Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

"""

# dictionary to hold the relationship of meters to another measure like feet (ft) or miles (mi)
distance_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}


# def to get and validate user input
def get_distance_input():
    while True:
        user_distance = input('Enter the distance you would like to convert: ')
        measure = input('Enter mi for miles, ft for feet, km for kilometers: ')
        try:
            user_distance = float(user_distance)
            break
        except ValueError:
            print('Invalid entry, you must enter a number.')
    return user_distance, measure


# calculate and return the converted distance
def convert_distance():
    distance, measure = get_distance_input()
    return f"{distance} {measure} is {distance_dict[measure] * distance:.4f} meters."


if __name__ == '__main__':
    print(convert_distance())
