class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Внесена сума:", amount)
        else:
            print("Невалидна сума!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Изтеглена сума:", amount)
        else:
            print("Недостатъчна наличност или невалидна сума!")

    def print(self):
        print("Собственик:", self.owner)
        print("Баланс:", self.balance, "лв.")


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Начислена лихва:", interest, "лв.")

    def print(self):
        super().print()
        print("Годишна лихва:", self.interest_rate, "%")


s1 = SavingsAccount("Иван Иванов", 1000, 5)
s2 = SavingsAccount("Мария Петрова", 2000, 3)

print("Първа сметка:")
s1.print()

print()
s1.add_interest()
s1.print()

print("\nВтора сметка:")
s2.print()

print()
s2.add_interest()
s2.print()