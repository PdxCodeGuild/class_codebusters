unit = {'feet': 0.3048}  # dictionary holds conversion rate
while True:  # allows try except to prevent incorrect entrie
    user = input('how many feet would you like converted to meters? :')
    try:
        user = float(user)
        break
    except:
        print('please enter numbers only')  # prevents incorrect entries

print((unit['feet'])*user)  # Converts and prints user input in meters
