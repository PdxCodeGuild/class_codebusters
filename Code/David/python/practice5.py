def even_even(nums):
    evennums = []  # list to append
    for num in nums:
        if num % 2 == 0:
            evennums.append(num)  # new list only has even numbers
        if (len(evennums) % 2) == 0:  # return true if length of list is even number
            return True
        else:  # return false if lenght of list is not even
            return False


def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    nums2 = nums[::-1]  # New list sliced beggining to end in reverse
    return(nums2)  # return new list


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    common = []


def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.


def combine(nums1, nums2):

    def test_combine():
        assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    ...


def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    nums2 = sum(nums)
    nums3 = nums2 / len(nums)
    return nums3


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    while '' in mylist:
        mylist.remove('')
    return mylist


def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    nums3 = [nums1[0], nums2[0]]
    nums4 = [nums1[1], nums2[1]]
    nums5 = [nums1[2], nums2[2]]
    nums6 = [nums3, nums4, nums5]
    return nums6


def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    nums4 = []


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [
        5, 2, 3, 4, 5, 1, 7, 6, 3]


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    ...


def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n):
    x = n
    while n > 1:
        n -= 1
    x *= n
    return x


def test_factorial():
    assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    ...


def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]
