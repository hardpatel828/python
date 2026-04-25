# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and
# customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:

    def __init__(self, account_number, customer_name, date_of_opening, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount(101, "Hard Patel", "06-08-2024", 5000)

account.check_balance()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()
