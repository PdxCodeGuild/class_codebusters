
dollar_amount = float(input('Enter a dollar amount: '))

pennies = int(dollar_amount * 100)
quarters = pennies // 25
pennies %= 25
dimes = pennies // 10
pennies %= 10
nickels = pennies // 5
pennies %= 5


print(f'{quarters} quarters {dimes} dimes {nickels} nickels {pennies} pennies')
