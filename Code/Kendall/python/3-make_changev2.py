coins = [
    ('dollar-coin', 'dollar-coins', 100),
    ('half-dollar', 'half-dollars', 50),
    ('CodeBuster', 'CBCs', 42),
    ('quarter', 'quarters', 25),
    ('dime', 'dimes', 10),
    ('nickels', 'nickels', 5),
    ('penny', 'pennies', 1)
]

# Get input
amount = input("Enter an amount: $")

# Convert to total pennies
amount = float(amount)
cents = int(amount * 100)

output = []

for coin in coins:
    # coin[0] = coin name
    # coin[1] = coin plural
    # coin[2] = coin value
    n_coins = cents // coin[2]
    cents %= coin[2]
    if n_coins > 0:
        if n_coins > 1:
            output.append(f'{n_coins} {coin[1]}')
        else:
            output.append(f'{n_coins} {coin[0]}')

print(",".join(output))
