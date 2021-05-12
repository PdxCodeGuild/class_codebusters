

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
car_brands.pop(-2)

del car_brands[0]
# del car_brands    # removes list

car_brands.extend(['lexus', 'gmc', 'chevy', 'subaru'])
car_brands.insert(0, 'jaguar')

car_brands[0], car_brands[2] = car_brands[2], car_brands[0]

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
new_nums = sorted(nums)  # Creates a new sorted list
newer_nums = reversed(nums)


print(new_nums)
