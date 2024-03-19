# Завдання 2
# Реалізуйте клас "Кошик для покупок" з можливістю
# додавання товарів та підрахунку загальної вартості.
# Застосуйте інкапсуляцію для забезпечення правильності
# обробки даних.
class ShoppingCart:
    def __init__(self):
        self.__items = []
    def add_item(self, name, price):
        self.__items.append((name, price))

    def total_price(self):
        total = 0
        for _, price in self.__items:
            total += price
        return total

cart = ShoppingCart()
cart.add_item("Апельсин", 20)
cart.add_item("Абрикос", 10)
print("Загальна вартість:", cart.total_price())