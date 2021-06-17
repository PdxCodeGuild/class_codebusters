# define a list

my_list = []
another_list = list()
my_nums = [1, 2, 3, 4, 5]

# print(my_nums[1])
# print(my_nums[-1])
# print(my_nums[1:3])


car_brands = ['Ford', 'Honda', 'Toyoa', 'Tesla', 'Volkswagen', 'Audi', 'BMW', 'Mini', 'Saturn', 'Oldsmobile',
              'Jeep']

# print(car_brands[-1:-4:-1])
# print(car_brands[-3:])

# print(len(car_brands))

print(car_brands[-1:-4:-1] == car_brands[-3:])

# list comprehension
nums = [3, 1, 5, 6]

# doubled_nums = []
# for num in nums:
#     doubled_nums.append(num*2)

doubled_nums = [num * 2 for num in nums]

print(doubled_nums)

