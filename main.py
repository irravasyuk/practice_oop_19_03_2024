# Створіть клас "Комп'ютер", який має зберігати
# інформацію про процесор, ОЗУ та відеокарту. Застосуйте
# інкапсуляцію для захисту цих даних від змін
class Computer:
    def __init__(self, processor, ram, gpu):
        self.__processor = processor
        self.__ram = ram
        self.__gpu = gpu

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_gpu(self):
        return self.__gpu

    def set_processor(self, processor):
        self.__processor = processor

    def set_ram(self, ram):
        self.__ram = ram

    def set_gpu(self, gpu):
        self.__gpu = gpu

mycomputer = Computer("Core i9 13900K", "32GB", "NVIDIA GeForce RTX 3080 10GB GDDR6X")
print("Процесор:", mycomputer.get_processor())
print("ОЗУ:", mycomputer.get_ram())
print("Відеокарта:", mycomputer.get_gpu())

mycomputer.set_ram("16GB")
print("Оновлена ОЗУ:", mycomputer.get_ram())
