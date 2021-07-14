

car = {
    'color': 'red',
    'doors': 4,
    'mpg': 30,
    'trims': ['ls', 'ex', 'super fantastic'],
    # 2: "secret stuff",
    # ('hello', 'world'): "Hello World"
}

# print(car.get('wheel_size', 'black'))

# Add new key: value
car['year'] = 2021

# Update key: value
car['year'] = 2020

# remove key: value
del car['mpg']

# for loop, loops over keys
# for key in car:
#     print(key)
#     print(car[key])


# update dictionary
car.update({'seats': 5})
car.update({'seats': 2})

# .keys()
# for key in car.keys():
#     print(key)

# .values()
# for value in car.values():
#     print(value)

# .items()
# for key, value in car.items():
#     print(key, value)


# hello = {i: "hello" for i in range(10)}
hello = {}
for i in range(10):
    hello[i] = "hello"


# print(hello)

# prices = {}
# while True:
#     key = input("Enter a fruit: ")
#     if key == "done":
#         break
#     value = input("Enter a price: ")

#     # prices[key] = value
#     prices.update({key: value})

# print(prices)


contacts = [
    {
        'first_name': 'Bill',
        'last_name': 'Personson',
        'address': {
            'street': '123 N ave',
            'city': 'Portland',
            'state': 'OR'
        }
    },
    {
        'first_name': 'Joe',
        'last_name': 'Humanson',
        'address': {
            'street': '124 N ave',
            'city': 'Portland',
            'state': 'OR'
        }
    }
]

# print(contacts[0]['address']['street'])
name = input("Enter contact name: ").title()
not_found = True
for contact in contacts:
    if contact['first_name'] == name:
        not_found = False
        print(contact['address'])
        break
if not_found:
    print("Contact not found, enter data to add.")
    last_name = input("Enter the last name: ")
    street = input("Enter the street address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")

    contacts.append({
        'first_name': name,
        'last_name': last_name,
        'address': {
            'street': street,
            'city': city,
            'state': state
        }
    })
    print(contacts)
