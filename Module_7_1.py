# ЗАДАЧА "Учёт товаров"

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        try:
            file = open(self.__file_name, "r", encoding="utf-8")
            file_list = file.read()
            file.close()
            return file_list
        except FileNotFoundError:
            file = open(self.__file_name, "w", encoding="utf-8")
            file.close()
            print("Список товаров пуст")

    def add(self, *products):

        try:
            file = open(self.__file_name, "r", encoding="utf-8")
            file_list = file.read()
            file.close()
            for product in products:
                _products = self.get_products()
                if product.name in _products:
                    print(f"Продукт {product} уже есть в магазине'")
                else:
                    _file = open(self.__file_name, "a", encoding="utf-8")
                    _file.write(f"{product}\n")
                    _file.close()
        except FileNotFoundError:
            print(f"Файл '{self.__file_name}' не найден и поэтому только что был создан...")
            file = open(self.__file_name, "w", encoding="utf-8")
            for product in products:
                file.write(str(product) + "\n")
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

####################### дубль операции после создания файла
print("#" * 30)
print("Повторный прогон после создания файла\n")

s1.add(p1, p2, p3)
print(s1.get_products())