#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python list practice
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 05/10/21
#----------------------------------------------------#


# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.


def even_even(nums):
    even_num_count = 0
    for x in nums:
        if x%2 == 0:
            even_num_count += 1
    if even_num_count % 2 == 0:
        return True
    return False 



def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    # return list(reversed(nums))
    reversed_nums = nums.copy()
    for i in range(len(nums)):
        reversed_nums[i * -1] = nums[i - 1]
    return reversed_nums


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    return [ x for x in nums1 if x in nums2]

    # returned_list = []
    # for x in nums1:
    #     if x in nums2:
    #         returned_list.append(x)
    # return returned_list




def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    # return [x for x in nums1, y for y in nums2]
    new_nums = []
    for i in range(len(nums1)):
        new_nums.append(nums1[i])
        new_nums.append(nums2[i])
    return new_nums
    

def test_combine():
    assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    all_options = []
    for num in nums:
        nums_list_without_target = nums.copy()
        nums_list_without_target.remove(num)
        for i in range(len(nums_list_without_target)):
            if num + nums_list_without_target[i] == target:
                all_options.append([num, nums_list_without_target[i]])

    for pair in all_options:
        pair.sort()

    for pair in all_options:
        pair_list_without_target = all_options.copy()
        pair_list_without_target.remove(pair)
        while True:
            for i in range(len(pair_list_without_target)):
                if pair == pair_list_without_target[i]:
                    all_options.remove(pair)
                    break
            break
    
    # while to_be_removed != []:
    #     for pair in to_be_removed:
    #         all_options.remove(pair)
    #         to_be_removed.remove(pair)

        
    
    return all_options

find_pair([5, 6, 2, 3], 7) == [[2, 5]]
find_pair([5,6,2,3,1,4], 7) == [[2,5], [1,6], [3,4]]

def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [[2, 5]]
    assert find_pair([5,6,2,3,1,4], 7) == [[2,5], [1,6], [3,4]]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    return sum(nums)/len(nums)


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    return [letter for letter in mylist if letter != '']


def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    new_nums = []
    for i in range(len(nums1)):
        new_nums.append([nums1[i], nums2[i]])
    return new_nums
    


def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    mega_list = []
    for i in range(len(nums)):
        for i2 in nums[i]:
            mega_list.append(i2)
    return mega_list


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [5, 2, 3, 4, 5, 1, 7, 6, 3]


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    f 
    fib_list = [1]
    for x in range(n):
        f += f
        fib_list.append(f)
    return fib_list



def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n):
    for i in range(1, n):
        n = n*i
    return n


def test_factorial():
    assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    for num in nums:
        nums_without_target = nums.copy()
        nums_without_target.remove(num)
        for i in range(len(nums_without_target)):
            if num == nums_without_target[i]:
                nums.remove(nums_without_target[i])
    nums.sort()
    return nums
                    


def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]