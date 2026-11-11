
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(
        self,
        name: str,
        description: str,
        price: int | float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, value: int | float) -> None:
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass
