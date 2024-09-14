class Product:
    def __init__(self, name: str, weigt: float, category: str):
        self.name = name
        self.weigt = weigt
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigt}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):

        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for i in products:
            if str(i) not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()

            else:
                print(f'Продукт {str(i)} - уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
