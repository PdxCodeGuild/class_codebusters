def make_change(amount):
    amount = int(amount * 100)
    quarters = amount // 25
    amount -= quarters*25
    dimes = amount // 10
    amount -= dimes * 10
    nickles = amount // 5
    amount -= nickles * 5
    pennies = amount
    return quarters, dimes, nickles, pennies


print(make_change(2.25))
