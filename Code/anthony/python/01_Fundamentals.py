

greeting = "Hello"  # String
name = "Class CodeBusters"


# print(id(greeting))
greeting = greeting + name
# print(id(greeting))

# print(greeting)

x = 4   # Int
y = 1.0  # Float
z = x + y

person = {
    'first_name': 'John',
    'last_name': 'Doe'
}   # Dictionary
place = {
    'city': 'Portland',
    'state': 'Oregon'
}
# print(id(person))
# print(person | place)
person.update(place)
# print(id(person))
# print(update_result)

# print(person['first_name'])

# 0     # 1        # 2     # 3   # 4   # 5
animals = ['duck', 'goose', 'chicken', 4.7, True, None]

colors = ['red', 'blue', 'green']

# print(animals + colors)


# print(animals[1])  # goose
# print(animals[6])  # out of range
# print(animals[-1])  # None
# print(animals[-7])  # out of range

is_cool = False  # Boolean

not_cool = None  # None

maybe_cool = 0


# operators
x + y  # Add
x - y  # Subtract
x / 2  # divide
x * 2  # multiply
x ** 2  # Exponential
x // 2  # floor divide
x % 3  # modulus

# assignment operators
x = 4   # assignment
x += 2
y -= 1
x /= 2
x //= 2
y *= 4
y **= 4
z %= 1


# print(x % 3)

is_cool = False

name = input("Enter your name: ")
message = name

message = f"{name} is cool" if is_cool else f"{name} is not cool"
print(message)

# if is_cool:
#     message += " is cool"
# else:
#     message += " is not cool"

# print(message)

# if is_cool:
#     print(f"{name} is cool")
# else:
#     print(f"{name} is not cool")

# print(is_cool == True)
