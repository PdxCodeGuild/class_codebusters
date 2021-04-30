import math

# numbers = [3, 7, 4, 0]

# print(max(numbers))  # 7
# print(min(numbers))  # 0
# print(sum(numbers))  # 14

# print(math.ceil(4.00003))   # 5
# print(math.floor(3.999999))  # 3
# print(math.pi)


# if 48 % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# colors = ['red', 'blue', 'green', 'yellow', 'gray']
# index = 0
# while True:
#     user_input = input("Press enter to see next color")
#     if user_input == "":
#         print(f"Showing color {index}")
#         print(colors[index % len(colors)])
#         print(f"index is {index % len(colors)}")
#         index += 1
#     else:
#         break


def add(x, y):
    sum = x + y
    return sum


def test_add():
    assert add(3, 4) == 7
    assert add(12, -2) == 10


def subtract(num1, num2):
    solution = num1 - num2
    return solution


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(4, 6) == -2
