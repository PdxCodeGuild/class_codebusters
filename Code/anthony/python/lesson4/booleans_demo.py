
# Booleans
True
False

# not
# print(not True)  # False
# print(not False)  # True

# and
# print(False and True)   # False
# print(True and False)   # False
# print(False and False)  # False
# print(True and True)    # True

# or
# print(True or True)  # True
# print(True or False)   # True
# print(False or True)    # True
# print(False or False)   # False


# Comparison
# < less than
# > greater than
# <= less than equal
# >= greater than equal
# == equal to
# != not equal

# print(3 < 4)
# print('a' != 'b')
# print('4' == 4)

# print(True and 3 > 4)
# print(not(True and 3 > 4))

x = 4
y = 7
z = 10

# print(y > x and y < 10)
# print(x < y < z)
# print(x == 4 == 4)

# numbers = [2, 4, 6, 8, 10]
# print(4 not in numbers)

# a = 4
# b = a
# b += 1
# print(a is b)

# a = "bob"
# a += "!"
# b = "bob"
# b += "!"

# print(a is b)

# colors = ['blue', 'red', 'green']
# more_colors = colors

# colors.append('gray')
# print(colors is more_colors)
# print(hex(id(colors)), hex(id(more_colors)))

# conditionals
# numbers = [2, 4, 6, 8, 10]
# if 5 in numbers:
#     print('Hooray!')
# elif 7 in numbers:
#     print('Not even')
# elif 4 in numbers:
#     print('Even numbers!!!')
# elif 9 in numbers:
#     print('also not even')
# else:
#     print('Could not find your number')

# value = ""
# if "":
#     print("The value is truthy")
# else:
#     print("The value is falsey")


# amount = input("Enter the amount to convert: ")
# if amount:
#     print(amount)
# else:
#     print("You need to enter a valid amount")

while True:
    amount = input("Enter the amount to convert: ")
    while not amount:
        amount = input("Enter the amount to convert: ")
    try:
        amount = float(amount)
    except ValueError:
        continue
    else:
        break
