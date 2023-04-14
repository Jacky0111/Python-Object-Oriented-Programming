"""
This program defines a BankAccount class that has methods for getting the balance, depositing and withdrawing
money. An instance of this class is created with an initial balance of 1000. The balance is then printed and 500 is
deposited and the balance is printed again. Finally, 200 is withdrawn and the balance is printed again. The output
shows the balance after each of these operations.
"""


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