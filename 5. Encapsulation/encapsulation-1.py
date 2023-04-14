class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account = BankAccount(1000)
print(account.get_balance())

account.deposit(500)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())


'''
Output
------
1000
1500
1300
'''