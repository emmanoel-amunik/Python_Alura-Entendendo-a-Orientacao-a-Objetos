
class Account:

    def __init__(self, number, owner, balance, limit):
        print(f"Building object... {self}")
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit
