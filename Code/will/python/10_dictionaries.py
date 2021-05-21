
# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

# def create_contact(x, y):
#     dict = {}
#     dict['name'] = x
#     dict.update({'age': y})
#     return dict


# print(create_contact('Bob', 67))  # {'name': 'Bob', 'age': 67}
# print(create_contact('Linda', 34))  # {'name': 'Linda', 'age': 34}


# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

# def has_key(d, key):
#     #dict = {'a': 1, 'b': 2}
#     if key in d:
#         return True
#     else:
#         return False


# print(has_key({'a': 1, 'b': 2}, 'a'))  # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

# def is_empty(d):
#     # if len(d) == 0:
#     #   return True
#     if d == {}:
#         return True
#     else:
#         return False


# print(is_empty({}))  # True
# print(is_empty({'a': 1, 'b': 2}))  # False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

# def find_key(d, value):
#     for key in d:
#         if value == d[key]:
#             return key


# print(find_key({'a': 1, 'b': 2}, 1))  # a
# print(find_key({'a': 1, 'b': 2}, 3))  # None


# Reverse Dict ================================================================= Need to review
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

# def reverse_dict(d):
#     # return d.update({1:d.values()})
#     rev_dict = {value: key for (key, value) in d.items()}
#     return rev_dict


# print(reverse_dict({'a': 1, 'b': 2}))  # {1: 'a', 2: 'b'}

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.


# def merge(list1, list2):
#     merge_dict = dict(zip(list1, list2))
#     return merge_dict


# print(merge(['a', 'b'], [1, 2]))  # {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

# def remove_less_than_10(d):
#     new_dict = {}
#     for key in d:
#         if d[key] >= 10:
#             new_dict[key] = d[key]
#             #del new_dict[value]
#     return new_dict


# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12}))  # {'b': 15, 'c': 12}


# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_values(d):
    # Sum numbers dividie by length for each of the keys
    # Loop through each key'value pairs
    for key in d:

        # sum/len()

        # {'a': 4, 'b': 5, 'c': 3}
print(average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]}))
'''
# Merge Dictionaries =========================================================== 
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key

def merge_dictionaries(d1, d2):
    ...

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(merge_dictionaries(d1, d2)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ================================================================== 
# Write a function that takes a list of strings and counts of the number of occurances.

def count_votes(votes):
    ...
# votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
# print(count_votes(votes)) # {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}

# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.

def cart_total(prices, cart):
    ...
# prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
# cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]
# print(cart_total(prices, cart)) # 11.0

'''
