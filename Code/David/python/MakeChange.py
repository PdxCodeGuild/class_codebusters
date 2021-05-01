while True:
    message = input('enter dollar amount without dollar sign ')
    try:
        amount = float(message)
        break
    except ValueError:
        print('numbers and decimal only please')

amount *= 100  #total in pennies
a = int(amount) // 25  #total quarters

print("That is " + str(a) + " quarters,")
amount %= 25  #remainder after quarters
b = int(amount) // 10  #total dimes
print(str(b) + ' dimes')
amount %= 10  #remaider after dimes
c = int(amount) // 5  #total nickels
print(str(c) + " nickels")

amount %= 5  #remainder after nickels
d = int(amount) // 1  # total pennies
print(str(d) + " pennies")
