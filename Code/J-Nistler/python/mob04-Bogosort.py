#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Mob 04 - Bogosort
Jared Nistler
Richard Lee
Jesse V
Will Lu
Zack
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Bogo sort is one of the least efficient sorting algorithms imaginable!
 It works by generating random arrangements of a list, checking if the 
 list is sorted, and if it is, return it. For a list of 200 numbers, 
 there are 200! = 7.88*10^374 possible combinations, only one of them 
 is the sorted list.

random_list(n) generates and returns a list of length n, with random 
values between 0 and 100

shuffle(nums) randomly re-arranges a list

- iterate through the indices of the list
- for each index, generate a random index
- swap the elements at the two indices

is_sorted(nums) checks if a list is sorted

- iterate through the indices of the list
- if the element at the current index is greater than the element at 
the next index, the list isn't sorted, and you can return False
- if you get through the entire list and each element is less than or 
equal to the next element, the list is sorted, and you can return True


bogosort(nums) continues to generate random arrangements until the 
list is sorted

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#

import random
import time

#-----------------------------------------------#
# Begin Mob Code
#-----------------------------------------------#

'''
Defines a function that takes in an int (n) as an argument and returns
a list of length n, with random values between 0 and 100
'''
def random_list(n):
    rand_list = []
    # iterate through the indices of the list
    for i in range(n):
        # add random int between 1 and 100
        rand_list.append(random.randint(0,100))
    return rand_list

#-----------------------------------------------#

'''
Defines a function that takes in a list as an argument and returns
that list with its items shuffled to random indexes
'''
def shuffle(nums):
            
    # iterate through the indices of the list
    for i in range(len(nums)):
        # for each index, generate a random index
        temp_index = random.randint(0,len(nums)-1)
        # swap the elements at the two indices
        temp_var = nums[temp_index]
        nums[temp_index] = nums[i]
        nums[i] = temp_var
    return nums

#-----------------------------------------------#

'''
Defines a function that takes in a list as an argument and returns
True if the list is sorted from least to greatest, False otherwise.
'''
def is_sorted(nums):
    # iterate through the indices of the list
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

#-----------------------------------------------#

'''
Defines a function that takes in a list as an argument and 
randomly shuffles the list until it is sorted from least 
to greatest.
'''
def bogosort(nums):
    start_time = time.time()
    count = 0
    sorted = False
    while sorted != True:
        shuff_list = shuffle(nums)
        print(shuff_list)
        sorted = is_sorted(shuff_list)
        count += 1
    end_time = time.time()
    return f'''
    You sorted the list in {count} attempts!
    It took {end_time - start_time:0.2f} seconds'''

#-----------------------------------------------#
# Testing
#-----------------------------------------------#

test_num = 11
test_list = random_list(test_num)
print(test_list)
print(bogosort(test_list))


# print(is_sorted([0,1,2,3]))
# print(is_sorted([0,1,5,3]))