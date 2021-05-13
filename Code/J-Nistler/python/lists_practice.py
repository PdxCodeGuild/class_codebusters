# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.


def even_even(nums):
    even_nums = []
    # put even numbers into new list
    for num in nums:
        if num % 2:
            pass
        else:
            even_nums.append(num)
    # if number of even numbers is odd, return false. Else True.
    if len(even_nums) % 2:
        return False
    else:
        return True


def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    reverse_list = []
    for i in range(len(nums)):
        reverse_list.append(nums[-(i+1)])
    return reverse_list


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]
    # Add test case
    assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 24]) == [24, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    common_list = []
    for num in nums1:
        if num in nums2:
            common_list.append(num)
    return common_list


def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    result_list = []
    for i in range(len(nums1)):
        result_list.extend([nums1[i], nums2[i]])
    return result_list


def test_combine():
    assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list
# that sum to a target number. 
# Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    # result_pairs = []
    for num in nums:
        delta = target - num
        if delta in nums:
            return[num, delta]
            # result_pairs.append([num, delta])
            # nums.remove(num)
            # nums.remove(delta)
    # return result_pairs


def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    total = 0
    for num in nums:
        total += num
    return total // len(nums)


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    result_list = []
    for i in range(len(mylist)):
        if mylist[i]:
            result_list.append(mylist[i])
    return result_list

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']

# Merge
# Write a function that merges two lists into a single list, 
# where each element of the output list is a list containing 
# two elements, one from each of the input lists.

def merge(nums1, nums2):
    result_list = []
    for i in range(len(nums1)):
        result_list.append([nums1[i], nums2[i]])
    return result_list



def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    result_list = []
    for list in nums:
        result_list.extend([num for num in list])
    return result_list


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [5, 2, 3, 4, 5, 1, 7, 6, 3]

# Fibonacci
# Write a function that takes `n` as a parameter, and returns a 
# list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    result_list = []

    for i in range(n):
        if i == 0 or i == 1:
            result_list.append(1)
        else:
            result_list.append(result_list[i-1] + result_list[i-2])
    return result_list


def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.

# def factorial(n):
#     factorial_list = [num for num in range(n + 1)]
#     factorial_list.pop(0)

#     for num in range(len(factorial_list)):


#     return factorial_list

# print(factorial(5))

# def test_factorial():
#     assert factorial(5) == 120


# # Find Unique
# # Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


# def find_unique(nums):
#     ...


# def test_find_unique():
#     nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
#     assert find_unique(nums) == [12, 24, 35, 88, 120, 155]