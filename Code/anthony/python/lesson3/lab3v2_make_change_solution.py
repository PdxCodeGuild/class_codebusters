coins = [
    ('quarter', 'quarters', 25),
    ('half-dollar', 'half-dollars', 50),
    ('dime', 'dimes', 10),
    ('dollar-coin', 'dollar-coins', 100),
    ('nickel', 'nickels', 5),
    ('penny', 'pennies', 1),
    ('CodeBuster', 'ÇBC', 42),
]

# Get input
amount = input("Enter an amount: $")

# Convert to total pennies
amount = float(amount)
pennies = int(amount * 100)

# Sort coins by value
coins.sort(key=lambda coin: coin[2], reverse=True)
# print(coins)


output = []
for coin in coins:
    # coin[0] = name of coin
    # coin[1] = plural name
    # coin[2] = coin value
    number_of_coins = pennies // coin[2]
    pennies %= coin[2]
    if number_of_coins:
        # if number_of_coins > 1:
        #     output.append(f"{number_of_coins} {coin[1]}")
        # else:
        #     output.append(f"{number_of_coins} {coin[0]}")
        output.append(
            f"{number_of_coins} {coin[0] if number_of_coins == 1 else coin[1]}")

print(", ".join(output))
