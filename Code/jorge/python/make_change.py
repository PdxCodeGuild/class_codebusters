# get user input
dollar_amount = float(input('Enter a dollar amount: '))
# convert coins
pennies = int(dollar_amount * 100)
# get quarters
quarters = pennies // 25
pennies %= 25
# get dimes
dimes = pennies // 10
pennies %= 10
# get nickels
nickels = pennies // 5
pennies %= 5


print(f'{quarters} quarters {dimes} dimes {nickels} nickels {pennies} pennies')
