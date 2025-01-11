class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read().strip()
                return products
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_product_names = {line.split(', ')[0] for line in existing_products}

        for product in products:
            if product.name in existing_product_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Выводит: Spaghetti, 3.4, Groceries

    s1.add(p1, p2, p3)  # Добавляем продукты в магазин

    print(s1.get_products())  # Выводит все продукты из файла

