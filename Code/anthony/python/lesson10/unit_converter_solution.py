"""
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
Version 3
Add support for yards, and inches.
"""

units_in_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
    'cm': .01
}


def check_measurement(measurement):
    while True:
        if measurement in units_in_meters:
            return measurement
        else:
            measurement = input(
                f"Invalid entry. Enter {', '.join(units_in_meters.keys())}: ")


def check_amount(amount):
    while True:
        if amount.isdigit():
            return int(amount)
        elif amount.replace('.', '', 1).isdigit():
            return float(amount)
        else:
            amount = input(
                "Invalid entry. Enter a number with or without decimals.")


"""Version 4
Now we'll ask the user for the:
[x] distance (value)
[x] starting units
[x] units to convert to.
[x] convert amount into meters
[x] convert meters into out_unit
"""

units = ', '.join(units_in_meters.keys())

amount = check_amount(input("Enter an amount: "))
in_unit = check_measurement(
    input(f"Enter a starting unit. {units}: "))
out_unit = check_measurement(
    input(f"Enter unit to convert to {units}: "))

# amount = 10
# in_unit = "ft"
# out_unit = "yd"


in_meters = amount * units_in_meters[in_unit]

output = in_meters / units_in_meters[out_unit]

output = round(output, 4)
if output.is_integer():
    output = int(output)

print(f"{amount} {in_unit} is {output} {out_unit}")
