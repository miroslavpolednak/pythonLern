# %%
class Product():
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price have to be possive")
        self.price = value


product = Product(50)
product2 = Product(-1)
product2.price = 20
