# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

from turtle import reset


def create_contact(name, age):
    dict = {}
    dict['name'] = name
    dict.update({'age': age})

    return dict
    # return {'name': name, 'age': age}


def test_create_contact():
    assert create_contact('Bob', 67) == {'name': 'Bob', 'age': 67}
    assert create_contact('Linda', 34) == {'name': 'Linda', 'age': 34}

# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.


def has_key(d, key):
    # if key in d:
    #     return True
    # else:
    #     return False

    return key in d


def test_has_key():
    assert has_key({'a': 1, 'b': 2}, 'a') == True
    assert has_key({'a': 1, 'b': 2}, 'c') == False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.


def is_empty(d):
    if d:
        return False
    else:
        return True

    # return not bool(d)


def test_is_empty():
    assert is_empty({}) == True
    assert is_empty({'a': 1, 'b': 2}) == False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.


def find_key(d, value):
    # return ''.join([key for key, val in d.items() if val == value]) if ''.join(
    #     [key for key, val in d.items() if val == value]) != '' else None

    for key in d:
        if d[key] == value:
            return key
    return None


def test_find_key():

    assert find_key({'a': 1, 'b': 2}, 1) == 'a'
    assert find_key({'a': 1, 'b': 2}, 3) == None

# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.


def reverse_dict(d):
    # result_dict = {}
    # for key in d:
    #     result_dict[d[key]] = key
    # return result_dict

    result_dict = {}
    for key, value in d.items():
        result_dict[value] = key
    return result_dict


def test_reverse_dict():
    assert reverse_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.


def merge(list1, list2):
    # result_dict = {}
    # for i in range(len(list1)):
    #     result_dict[list1[i]] = list2[i]
    # return result_dict

    # d = {}
    # for x, y in zip(list1, list2):
    #     d[x] = y
    # return d

    return dict(zip(list1, list2))


def test_merge():
    assert merge(['a', 'b'], [1, 2]) == {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    # return {key: value for key, value in d.items() if value > 10}
    new_d = {}
    for key, value in d.items():
        if value >= 10:
            new_d[key] = value
    return new_d


def test_remove_less_than_10():
    assert remove_less_than_10({'a': 5, 'b': 15, 'c': 12}) == {
        'b': 15, 'c': 12}

# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.


def average_values(d):
    # d_average = {}
    # for key in d:
    #     added = 0
    #     amount = 0
    #     for num in d[key]:
    #         added += num
    #         amount += 1
    #     avg = added / amount
    #     d_average[key] = int(avg)
    # return d_average

    result_dict = {}
    for key in d:
        avg_list = sum(d[key]) // len(d[key])
        result_dict[key] = avg_list
    return result_dict


def test_average_values():
    assert average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]}) == {
        'a': 4, 'b': 5, 'c': 3}

# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key


def merge_dictionaries(d1, d2):
    for key in d2:
        if key in d1:
            d1[key] += d2[key]
        else:
            d1[key] = d2[key]

    return d1


def test_merge_dictionaries():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    assert merge_dictionaries(d1, d2) == {
        'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.


def count_votes(votes):
    # d = {}
    # for name1 in votes:
    #     count = 0
    #     for name2 in votes:
    #         if name2 == name1:
    #             count += 1
    #     d[name1] = count
    # return d

    # d = {}
    # for name in votes:
    #     if name not in d:
    #         d[name] = 1
    #     else:
    #         d[name] += 1
    # return d

    return {name: votes.count(name) for name in votes}


def test_count_votes():
    votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie',
             'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
    assert count_votes(votes) == {'john': 4,
                                  'johnny': 3, 'jackie': 2, 'jamie': 4}

# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.


def cart_total(prices, cart):
    total = 0
    for d in cart:
        total += prices[d['item']] * d['quantity']
    return total


def test_cart_total():
    prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
    cart = [{'item': 'apples', 'quantity': 3},
            {'item': 'kiwis', 'quantity': 4}]
    assert cart_total(prices, cart) == 11.0
