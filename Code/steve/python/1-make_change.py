'''
Let's convert a dollar amount into a number of coins.
The input will be the total amount, the output will be
the number of quarters, dimes, nickles, and pennies.
Always break the total into the highest coin value first,
resulting in the fewest amount of coins.
First convert the dollar amount (1.36) into the total number of pennies (136),
then use floor division //, which throws away the remainder. 10/3 is 3.333333,
10//3 is 3.
'''


def make_change():
    while True:
        amnt = input('Enter a dollar amount: ')
        try:
            amnt = float(amnt)
            break
        except ValueError:
            print('Invalid entry')

    pennies = amnt * 100
    qtrs = pennies // 25
    pennies -= (qtrs * 25)
    dimes = pennies // 10
    pennies -= dimes * 10
    nickles = pennies // 5
    pennies -= nickles * 5

    change = f'${amnt:.2f} is {int(qtrs)} quarters, {int(dimes)} dimes, {int(nickles)} nickles, and {int(pennies)} pennies.'
    return change


print(make_change())
