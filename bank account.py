class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def display_balance(self):
        print(f"Account Holder: {self.name}\nBalance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        account = Account(name, initial_balance)
        self.accounts[name] = account
        print(f"Account created for {name} with an initial balance of {initial_balance}")

    def get_account(self, name):
        return self.accounts.get(name)

    def execute_transaction(self, name, transaction):
        account = self.get_account(name)
        if account:
            transaction(account)
        else:
            print("Account not found.")

    def menu(self):
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        return input("Enter your choice: ")

bank = Bank()

while True:
    choice = bank.menu()

    actions = {
        '1': lambda: bank.create_account(input("Enter account holder's name: "), float(input("Enter initial balance: "))),
        '2': lambda: bank.execute_transaction(input("Enter account holder's name: "), lambda acc: acc.deposit(float(input("Enter deposit amount: ")))),
        '3': lambda: bank.execute_transaction(input("Enter account holder's name: "), lambda acc: acc.withdraw(float(input("Enter withdrawal amount: ")))),
        '4': lambda: bank.execute_transaction(input("Enter account holder's name: "), lambda acc: acc.display_balance()),
        '5': exit
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")
