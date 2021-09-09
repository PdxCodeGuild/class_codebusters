"""
Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it

Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions.
"""
from datetime import datetime


class Transaction:
    def __init__(self, date, transaction_type, amount, balance):
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __repr__(self):
        return f"{self.date} -- {self.transaction_type} {self.amount} {self.balance}"


class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name
        self.transactions = []

    def __repr__(self):
        return f"Welcome {self.name}, your balance is ${self.balance}"

    def total_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(
            datetime.now(), 'deposit', amount, self.balance)
        self.transactions.append(transaction)
        return f"Deposit of ${self.balance} has been posted."

    def withdraw(self, amount):
        if amount > self.balance:
            return f'Withdraw denied. Balance remaining ${self.balance}'
        else:
            self.balance -= amount
            transaction = Transaction(
                datetime.now(), 'withdraw', -amount, self.balance)
            self.transactions.append(transaction)
            return f'Withdrew ${amount}. Balance remaining ${self.balance}'


account = Account("Neil")
print(account.deposit(1000000))
print(account.withdraw(2000000))
print(account.withdraw(50))

for item in account.transactions:
    print(f"{item.date.strftime('%d%B%Y')} -- {item.transaction_type}) {item.amount}. Balance: {item.balance}")
