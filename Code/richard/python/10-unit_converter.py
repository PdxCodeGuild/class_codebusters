# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. 
# Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
# Below is some sample input/output.

'''
userInput = int(input("What is the distance in feet? "))
def feet_to_meter(ft):
    return ft * 0.3048

print(feet_to_meter(userInput))
'''
# Version 2
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
# The units we'll allow are feet, miles, meters, and kilometers.
'''
userUnits = input("What unit will you input? feet, miles, meters or kilometers ").lower()
userDistance = int(input("What is the distance? "))

def convert_to_meters(units,dist):
    if units == "feet":
        return f"{dist} {units} is {dist * 0.3048}m"
    elif units == "miles":
        return f"{dist} {units} is {dist * 1609.34}m"
    elif units == "meters":
        return f"{dist} {units} is {dist}m"
    elif units == "kilometers":
        return f"{dist} {units} is {dist * 1000}m"
    else:
        return "You did not enter a valid input."

print(convert_to_meters(userUnits,userDistance))
'''
# Version 3
# Add support for yards, and inches.
'''
userUnits = input("What unit will you input? feet, miles, meters, kilometers, yards or inches ").lower()
userDistance = int(input("What is the distance? "))

def convert_to_meters(units,dist):
    if units == "feet":
        return f"{dist} {units} is {dist * 0.3048}m"
    elif units == "miles":
        return f"{dist} {units} is {dist * 1609.34}m"
    elif units == "meters":
        return f"{dist} {units} is {dist}m"
    elif units == "kilometers":
        return f"{dist} {units} is {dist * 1000}m"
    elif units == "yards":
        return f"{dist} {units} is {dist * 0.9144}m"
    elif units == "inches":
        return f"{dist} {units} is {dist * 0.0254}m"
    else:
        return "You did not enter a valid input."

print(convert_to_meters(userUnits,userDistance))
'''
# Version 4
# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# You can think of the values for the conversions as elements in a matrix, where the rows will be the 
# units you're converting from, and the columns will be the units you're converting to. Along the 
# horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

userUnits = input("What unit will you input? feet, miles, meters, kilometers, yards or inches ").lower()
userDistance = int(input("What is the distance? "))
userConvert = input("What unit will you want output? feet, miles, meters, kilometers, yards or inches ").lower()


def convert_to_meters(units,dist,conv):
    convert_unit = {'feet':0.3048,'miles':1609.34,'meters':1,'kilometers':1000,'yards':0.9144,'inches':0.0254}
    if units in convert_unit:
        return f"{dist} {units} is {(dist * convert_unit[units]) / convert_unit[conv]} {conv}"
    else:
        return "You did not enter a valid input."

print(convert_to_meters(userUnits,userDistance,userConvert))