
num = 4
greeting = "Hello"


def subtract(num, b=0, c=0):
    print(greeting)
    print(num)
    return num - b - c


# subtract(8, c=2, b=4)
# subtract(10)

def say_something(*args, **kwargs):
    """This function will print all args"""
    args = " ".join(args)  # join arguments together
    print(kwargs)
    return True, False


# say_something("Hello", "Goodbye", "Hello again",
#               "this", "is", "another", "argument")

# say_something(dog="woof", cat="meow", bird="chirp")

# return_value, is_false = say_something("hello")
# print(return_value, is_false)

# def count_up(n, count=0):
#     if count == n:
#         return 1
#     print(count)
#     count_up(n, count + 1)


# def count_down(n):
#     count_up(n)
#     if n == 0:
#         return 1
#     print(n)
#     count_down(n - 1)


# count_down(5)

# def add(a, b):
#     return a + b


# print(add(5, 6))

# def add_more(a, b): return a + b


# print(add_more(5, 6))

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# def doubled(nums): return [x*2 for x in nums]


# print(doubled(nums))

# say_something()
# print(print.__doc__)


def add(a: int, b: int) -> int:
    """Adds argument a and argument b"""
    return a + b


print(add("hello ", "world"))
