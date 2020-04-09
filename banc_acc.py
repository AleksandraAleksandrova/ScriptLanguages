class Account:
    def __init__(self, name, account_id, balance):
        self.name=name
        self.account_id=account_id
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount

    def tegli(self, suma):
        self.balance-=suma

    def display(self):
        print("Name {self.name}, Account: {self.account_id}, Balance:{self.balance}")

acc = Account("Nasko", "1234", 150)
print(acc.balance)
acc.deposit(200)
print(acc.balance)
acc.tegli(200)
print(acc.balance)
print(acc.display())


