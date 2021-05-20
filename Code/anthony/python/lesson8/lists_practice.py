

# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.


def even_even(nums):
    evens = 0
    for num in nums:
        if num % 2 == 0:
            evens += 1
    # if evens % 2 == 0:
    #     return True
    # else:
    #     return False
    return evens % 2 == 0


def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


# Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    # return reversed(nums)
    # return nums[::-1]
    reverse_list = []
    for i in range(len(nums)):
        reverse_list.append(nums[-(i + 1)])
        # reverse_list.append(nums[len(nums) - i - 1])
    return reverse_list


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.


def common_elements(nums1, nums2):
    # return [x for x in nums1 if x in nums2]
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
    combine_list = []
    for let, num in zip(nums1, nums2):
        # combine_list.append(let)
        # combine_list.append(num)
        combine_list.extend([let, num])
    return combine_list

    # for i in range(len(nums1)):
    #     combine_list.extend([nums1[i], nums2[i]])

    # return combine_list


# [('a', 1), ('b', 2), ('c', 3)]


def test_combine():
    assert combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.


def find_pair(nums, target):
    # all_options = []
    # for num in nums:
    #     nums_list_without_target = nums.copy()
    #     nums_list_without_target.remove(num)
    #     for i in range(len(nums_list_without_target)):
    #         if num + nums_list_without_target[i] == target:
    #             all_options.append([num, nums_list_without_target[i]])
    # for pair in all_options:
    #     pair.sort()
    # for pair in all_options:
    #     pair_list_without_target = all_options.copy()
    #     pair_list_without_target.remove(pair)
    #     while True:
    #         for i in range(len(pair_list_without_target)):
    #             if pair == pair_list_without_target[i]:
    #                 all_options.remove(pair)
    #                 break
    #         break
    # return all_options

    # pair = []
    # i = 0
    # while i < len(nums):
    #     j = i + 1
    #     while j < len(nums):
    #         if nums[i] + nums[j] == target:
    #             tup = (nums[i], nums[j])
    #             pair.append(tup)
    #         j += 1
    #     i += 1
    # return pair

    pairs = []
    for num in nums:
        difference = target - num
        if difference in nums:
            if num not in pairs:
                pairs.extend([num, difference])
    return pairs


def test_find_pair():
    assert find_pair([5, 6, 2, 3], 7) == [5, 2]
    assert find_pair([5, 6, 2, 3, 1, 4], 7) == [5, 2, 6, 1, 3, 4]
    # assert find_pair([5, 6, 2, 3], 7) == [(5, 2)]
    # assert find_pair([5, 6, 2, 3, 1, 4], 7) == [(5, 2), (6, 1), (3, 4)]


# Average
# Write a function to find the average of a list of numbers


def average(nums):
    # total = 0
    # for num in nums:
    #     total += num
    # return total / len(nums)

    # divisor = len(nums)
    # total_sum = 0
    # for num in nums:
    #     total_sum += num
    # return int(total_sum / divisor)

    return int(sum(nums)/len(nums))


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3


# Remove Empty
# Write a function to remove all empty strings from a list.


def remove_empty(mylist):
    # while "" in mylist:
    #     mylist.remove("")

    # return mylist

    return [letter for letter in mylist if letter]


def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']


# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    # output = []
    # for x, y in zip(nums1, nums2):
    #     output.append([x, y])
    # return output

    # merge_list = []
    # for i in range(len(nums1)):
    #     my_list = [nums1[i], nums2[i]]
    #     merge_list.append(my_list)
    # return merge_list

    return [[x, y] for x, y in zip(nums1, nums2)]


def test_merge():
    assert merge([5, 2, 1], [6, 8, 2]) == [[5, 6], [2, 8], [1, 2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.


def combine_all(nums):
    result_list = []
    # for _list in nums:
    #     result_list.extend(_list)

    # return result_list

    for _list in nums:
        for num in _list:
            result_list.append(num)
    return result_list

    # for _ in range(10):
    #     print("hello")


def test_combine_all():
    assert combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]) == [
        5, 2, 3, 4, 5, 1, 7, 6, 3]


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


# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)


def test_fibonacci():
    # output = []
    # n = 0
    # while n < 8:
    #     output.append(fibonacci(n))
    #     n += 1

    # assert output == [1, 1, 2, 3, 5, 8, 13, 21]
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.


def factorial(n):
    # fac = n
    # while n > 1:
    #     n -= 1
    #     fac *= n
    # return fac

    # total = 1
    # factorial_list = [num for num in range(n+1)]
    # factorial_list.pop(0)
    # for i in range(len(factorial_list)):
    #     total *= factorial_list[i]
    # return total

    zip()
    output = n
    for i in reversed(range(1, n+1)):
        if i > 1:
            output *= i - 1

    return output


def test_factorial():
    assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


def find_unique(nums):
    # unique_list = []
    # for n in nums:
    #     if n not in unique_list:
    #         unique_list.append(n)
    # return unique_list

    # for num in nums:
    #     nums_without_target = nums.copy()
    #     nums_without_target.remove(num)
    #     for i in range(len(nums_without_target)):
    #         if num == nums_without_target[i]:
    #             nums.remove(nums_without_target[i])
    # return sorted(nums)

    return sorted(list(set(nums)))


def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]
