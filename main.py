# Завдання 1
# Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
# "email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
# дані можна отримати лише через методи класу.
class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_full(self):
        return f"Name:{self.__name}, Age:{self.__age}, Email:{self.__email}"


user = User("Вікторія", 19, "viktoria@gmail.com")
print("Інформація про користувача: ", user.get_full())

print("Змінюємо інформацію:")
user.set_name("Юлія")
user.set_age(22)
user.set_email("julia@gmail.com")
print(f"Оновлена інформація про користувача: {user.get_full()}")