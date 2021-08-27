class Product:
    def __init__(self,price):
        self.__price = price
    
    @property
    def Price(self):
        return self.__price

    @Price.setter
    def price(self,value):
        if value<0:
            raise ValueError("Price cannot be negative")
        self.__price = Value


product = Product(300)

