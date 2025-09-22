class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} . New balance : {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"withdraw {amount}. New balance : {self.balance}"

    def get_balance(self):
        return f"Current balance :{self.balance}"

    def __str__(self):
        return f"Bank Account of {self.owner} | Balance : {self.balance}"


account = BankAccount("Qasem", 1000)
print(account)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))
print(account.get_balance())
