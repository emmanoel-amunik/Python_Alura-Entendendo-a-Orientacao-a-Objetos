
class Account:

    def __init__(self, number, owner, balance, limit):
        print(f"Building object... {self}")
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def statement(self):
        print(f"The Balance is {self.balance} of the owner {self.owner}.")

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
