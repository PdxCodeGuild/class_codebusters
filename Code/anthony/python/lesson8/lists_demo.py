

# Define a list
my_list = []
another_list = list()
my_nums = [2, 3, 4, 5]

# print(my_nums[1])
# print(my_nums[-1])
# print(my_nums[1:3])
# print(my_nums[100])   # index out of range

car_brands = ["ford", ["honda", "acura"], "toyota", "tesla", "volkswagen",
              "audi", "bmw", "mini", "saturn", "oldsmobile", "jeep", "oldsmobile"]

# print(car_brands[-1:-4:-1])
# print(car_brands[-3:])

# print(len(car_brands))
# cars1 = car_brands[-1:-4:-1]
# cars2 = car_brands[-3:]
# cars1.sort()
# cars2.sort()
# print(cars1 == cars2)
# print(cars1 is cars2)


# print("bmw" in car_brands)  # True
# print("kia" in car_brands)  # False
# print("acura" in car_brands[1])  # True
# print(car_brands[1][0])     # honda

# car_brands.append("kia")
car_brands.insert(2, "kia")
while "oldsmobile" in car_brands:
    car_brands.remove("oldsmobile")
# car_brands.pop(-2)

del car_brands[0]
# del car_brands    # removes list

car_brands.extend(['lexus', 'gmc', 'chevy', 'subaru'])
car_brands.insert(0, 'jaguar')

car_brands[0], car_brands[2] = (car_brands[2], car_brands[0])
x, y = ("hello", "word")

# temp = car_brands[0]
# car_brands[0] = car_brands[2]
# car_brands[2] = temp

rival_brands = car_brands.copy()

# rival_brands[0] = ''


# print(car_brands.index('bmw'))
del rival_brands[1]
# rival_brands.reverse()
# rival_brands.sort(reverse=True)

nums = [3, 1, 5, 6]
# nums.sort()   # Sorts original list
# new_nums = sorted(nums)  # Creates a new sorted list
# newer_nums = reversed(nums)

# print(new_nums)

# doubled_nums = []
# for num in nums:
#     doubled_nums.append(num*2)

# doubled_nums = [num * 2 for num in nums]

# print(doubled_nums)

# short_brands = []
# for brand in car_brands:
#     if brand.startswith('t') or brand.startswith('s'):
#         short_brands.append(brand)

# car_brands.pop(1)
# short_brands = [brand for brand in car_brands if brand.startswith(
#     't') or brand.startswith('s')]
# print(short_brands)

"""
[
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2]
]
"""

# grid = []
# for x in range(3):
#     row = []
#     for y in range(3):
#         row.append(y)
#     grid.append(row)

# grid = [[y for y in range(3)] for x in range(3)]

# print(grid)


# dict_comp = {str(x): x for x in range(5)}
# print(dict_comp)


# contact_info = ('123 Main St', '503-555-1234', 'apt 123')
# # Throws TypeError
# contact_info = list(contact_info)
# contact_info[0] = '456 Water Ave'
# contact_info = tuple(contact_info)
# print(contact_info)


def say_hello(name):
    return "Hello", name


greeting, name = say_hello("Bill")
print(greeting, name)
