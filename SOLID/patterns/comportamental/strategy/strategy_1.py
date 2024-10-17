"""
    Open/Closed Principle
    Entidades abertas para extensão, mas fechadas para modificação
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        ...


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    custom_discount = CustomDiscount(5)

    print('\nDesconto de 20%:')
    order = Order(1000, twenty_percent)
    print(f'De: R$ {order.total:.2f}'.replace('.', ','))
    print(f'Por: R$ {order.total_with_discount:.2f}'.replace('.', ','))

    print('\nDesconto de 50%:')
    order = Order(1000, fifty_percent)
    print(f'De: R$ {order.total:.2f}'.replace('.', ','))
    print(f'Por: R$ {order.total_with_discount:.2f}'.replace('.', ','))

    print('\nSem desconto:')
    order = Order(1000, no_discount)
    print(f'De: R$ {order.total:.2f}'.replace('.', ','))
    print(f'Por: R$ {order.total_with_discount:.2f}'.replace('.', ','))

    print('\nDesconto de 5%:')
    order = Order(1000, custom_discount)
    print(f'De: R$ {order.total:.2f}'.replace('.', ','))
    print(f'Por: R$ {order.total_with_discount:.2f}'.replace('.', ','))
