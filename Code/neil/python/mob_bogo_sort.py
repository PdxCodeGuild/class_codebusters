'''

Bogo Sort

Bogo sort is one of the least efficient sorting algorithms imaginable! It works by generating random arrangements of a list, checking if the list is sorted, and if it is, return it. For a list of 200 numbers, there are 200! = 7.88*10^374 possible combinations, only one of them is the sorted list.

random_list(n) generates and returns a list of length n, with random values between 0 and 100

shuffle(nums) randomly re-arranges a list

iterate through the indices of the list
for each index, generate a random index
swap the elements at the two indices
is_sorted(nums) checks if a list is sorted

iterate through the indices of the list
if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return True
bogosort(nums) continues to generate random arrangements until the list is sorted

'''
import random
import time

# random_list
def random_list(n):

    random_list = []

    for x in range(n):
        random_list.append(random.randint(0, 100))
    
    return random_list

# function for shuffling nums
def shuffle(nums):
    
    for i in range(len(nums)):
        temp_indice = random.randint(0, len(nums) -1)
        nums[i], nums[temp_indice] = (nums[temp_indice], nums[i])
    
    return nums

# function for sort
def is_sorted(nums):

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    
    return True

# function for bogosort(nums)
def bogosort(nums):

    counter = 0
    
    try:

        while is_sorted(nums) == False:
            counter += 1
            shuffle(nums)

    except KeyboardInterrupt:

        print(counter)

    print(f'It took {counter} amount of times to solve via bogo.')

num_list = random_list(3)
print(num_list)

shuffle(num_list)

start = time.time()
bogosort(num_list)
end = time.time()

print(end - start)