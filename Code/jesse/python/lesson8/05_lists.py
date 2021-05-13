# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.


def even_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count % 2 == 0


def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    reverse = []
    for num in reversed(nums):
        reverse.append(num)
    return reverse


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    common = []
    for num in nums1:
        if num in nums2:
            common.append(num)
    return common


def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):
    combined_list = []
    for let, num in zip(nums1, nums2):
        combined_list.append(let)
        combined_list.append(num)
    return combined_list


def test_combine():
    assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    pairs = []
    for num in nums:
        difference = target - num
        if difference in nums:
            if num not in pairs:
                pairs.append(num)
                pairs.append(difference)
    return pairs

print(find_pair([5, 6, 2, 3, 5, 2, 4], 7))

def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    sum = 0
    for num in nums:
        sum += num
    average = int(sum / len(nums))
    return average


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    for char in mylist:
        if char == '':
            mylist.remove(char)
    return mylist
    

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    output = []
    for x, y in zip(nums1, nums2):
        output.append([x, y])
    return output


def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    output = []
    for ls in nums:
        for num in ls:
            output.append(num)
    return output


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [5, 2, 3, 4, 5, 1, 7, 6, 3]


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    output = []
    fn = 0
    for i in range(n + 1):
        if i <= 1:
            output.append(fn)
            fn += 1        
        else:
            fn = output[i - 1] + output[i - 2]
            output.append(fn)
    output.remove(0)
    return output


def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n):
    output = n
    for i in reversed(range(1, n + 1)):
        if i > 1:
            output *= i - 1
    return output
        

def test_factorial():
    assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    output = []
    for num in nums:
        if num not in output:
            output.append(num)
    return output


def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]