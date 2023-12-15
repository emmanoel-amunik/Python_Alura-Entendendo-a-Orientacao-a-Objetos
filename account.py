
class Account:

    def __init__(self, number, owner, balance, limit):
        print(f"Building object... {self}")
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print(f"The Balance is {self.__balance} of the owner {self.__owner}.")

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    # gets
    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    # sets
    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit
