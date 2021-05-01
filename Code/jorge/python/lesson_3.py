numbers = [3, 7, 4, 8]

# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


# if 47 % 2 == 0:
#     print('number is even')
# else:
#     print('odd')


# colors = ['red', 'blue', 'green', 'yellow', 'gray']
# index = 0
# while True:
#     input("press enter to see the next color")
#     print(colors[index % len])


def add(x, y):
    sum = x + y + 1
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
