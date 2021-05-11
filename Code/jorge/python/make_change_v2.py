

coins = [

    ('dollar', 'dollars', 100),
    ('half-dollar', 'hald-dollars', 50),
    ('codbuster', 'codbusters', 42),
    ('quarter', 'quarters', 25),
    ('dime', 'dimes', 10),
    ('nickel', 'nickels', 5),
    ('penny', 'pennies', 1),
]

# Get input
amount = input('Enter an amount: $')
# Convert to toal pennies
amount = float(amount)
pennies = int(amount * 100)

output = []
for coin in coins:

    number_of_coins = pennies // coin[2]
    pennies %= coin[2]
    if number_of_coins:
        if number_of_coins > 1:
            output.append(f'{number_of_coins} {coin[1]}')
        else:
            output.append(f'{number_of_coins} {coin[0]}')

print(', '.join(output))
