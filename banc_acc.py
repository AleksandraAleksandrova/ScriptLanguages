class Account:
    def __init__(self, name, account_id, balance):
        self.name=name
        self.account_id=account_id
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount

    def tegli(self, suma):
        self.balance-=suma

acc = Account("Nasko", "1234", 150)
print(acc.balance)
acc.deposit(200)
print(acc.balance)
acc.tegli(200)
print(acc.balance)

