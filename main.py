class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Недостатньо коштів')
        else:
            self.balance -= amount
    def check_balance(self):
        return self.balance
acc = BankAccount('Vasya', 500)
acc.deposit(200)
acc.withdraw(100)
print(acc.check_balance())