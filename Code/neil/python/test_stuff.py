def reverse(nums):

    reversed_list = []

    for num in nums:
        reversed_list.append(nums.pop(-1))

    reversed_list.append(nums.pop(0))

    return reversed_list


# def test_reverse():
#     assert reverse([1, 2, 3]) == [3, 2, 1]
print(reverse([1, 2, 3]))