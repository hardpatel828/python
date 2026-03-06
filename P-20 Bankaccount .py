# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and
# customer_name, and methods like deposit, withdraw, and check_balance.

# Define BankAccount class
class BankAccount:

    # Constructor to initialize data
    def __init__(self, account_number, customer_name, date_of_opening, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    # Method to deposit amount
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    # Method to withdraw amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    # Method to check balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Create an object of BankAccount class
account = BankAccount(101, "Hard Patel", "06-08-2024", 5000)

# Perform operations
account.check_balance()
account.deposit(2000)
account.withdraw(1500)
account.check_balance()