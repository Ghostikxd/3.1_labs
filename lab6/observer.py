from abc import *
from typing import List


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, int):
        pass


class Observeroperation(metaclass=ABCMeta):
    @abstractmethod
    def add_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(Observeroperation):
    def __init__(self, price):
        self.price = price
        self.observers: List[Observer] = []

    def change_price(self, price):
        self.price = price
        self.notify()

    def add_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        self.observers.remove(o)

    def notify(self):
        for o in self.observers:
            o.update(self.price)


class Wholesaler(Observer):
    def __init__(self, obj: Observeroperation):
        self.product = obj
        obj.add_observer(self)

    def update(self, price):
        if price < 1000:
            print('Оптовик закупил товар по цене', price)
            self.product.remove_observer(self)


class Buyer(Observer):
    def __init__(self, obj: Observeroperation):
        self.product = obj
        obj.add_observer(self)

    def update(self, price):
        if price > 1000:
            print('Покупатель купил товар по цене', price)
            self.product.remove_observer(self)


if __name__ == '__main__':
    product = Product(1500)
    wholesaler = Wholesaler(product)
    buyer = Buyer(product)
    product.change_price(750)
    product.change_price(1200)
