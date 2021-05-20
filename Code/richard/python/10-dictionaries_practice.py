# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

def create_contact(name, age):
    return {"name" : name, "age": age}

def test_create_contact():
    assert(create_contact('Bob', 67))  == {'name': 'Bob', 'age': 67}
    assert(create_contact('Linda', 34)) == {'name': 'Linda', 'age': 34}

# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

def has_key(d, key):
    return key in d.keys()

def test_has_key():
    assert(has_key({'a': 1, 'b': 2}, 'a')) == True
    assert(has_key({'a': 1, 'b': 2}, 'c')) == False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

def is_empty(d):
    return False if d else True

def test_is_empty():
    assert(is_empty({})) == True
    assert(is_empty({'a': 1, 'b': 2})) == False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in 
# the dictionary, it should return `None`.

def find_key(d, value):
    for i in d:
        if d[i] == value:
            return i
    return None

def test_find_key():
    assert(find_key({'a': 1, 'b': 2}, 1)) == 'a'
    assert(find_key({'a': 1, 'b': 2}, 3)) == None

# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    reversedDict = {}
    for i in d:
        reversedDict[d[i]] = i
    return reversedDict

def test_reverse_dict():
    assert(reverse_dict({'a': 1, 'b': 2})) == {1: 'a', 2: 'b'}

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list 
# containing the keys, and the second containing the values.

def merge(list1, list2):
    mergedDict = {}
    for i in range(len(list1)):
        mergedDict[list1[i]] = list2[i]
    return mergedDict

def test_merge():
    assert(merge(['a', 'b'], [1, 2])) == {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    lessThan10 = {}
    for i in d:
        if d[i] >= 10:
            lessThan10[i] = d[i]
    return lessThan10

def test_remove_less_than_10():
    assert(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) == {'b': 15, 'c': 12}

# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_values(d):
    for i in d:
        d[i] = (sum(d[i])/len(d[i]))
    return d

def test_average_values():
    assert(average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]})) == {'a': 4, 'b': 5, 'c': 3}

# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each 
# added together if they have the same key

def merge_dictionaries(d1, d2):
    for i in d2:
        if i in d1.keys():
            d1[i] += d2[i]
        else:
            d1[i] = d2[i]
    return d1


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

def test_merge_dictionary():
    assert(merge_dictionaries(d1, d2)) == {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.

def count_votes(votes):
    voteDict = {}
    for i in votes:
        if i in voteDict.keys():
            voteDict[i] += 1
        else:
            voteDict[i] = 1
    return voteDict

votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']

def test_count_votes():
    assert(count_votes(votes)) == {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}

# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries 
# representing a cart and a dictionary representing prices.

def cart_total(prices, cart):
    total = 0
    for i in range(len(cart)):
        total += prices[cart[i]['item']] * cart[i]['quantity']
    return total


prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]

def test_cart_total():
    assert(cart_total(prices, cart)) == 11.0