# Створіть клас "Електронний Гаманець" додавши
# можливість видаляти та додавати гроші, а також перевіряти
# баланс.
class ElectronicWallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount

    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостатньо коштів.")

    def get_balance(self):
        return self.balance

wallet = ElectronicWallet()
print("Надійшли кошти:")
wallet.add_money(1000)
print("Баланс:", wallet.get_balance())

print("Витратили гроші:")
wallet.remove_money(100)
print("Баланс після витрат:", wallet.get_balance())