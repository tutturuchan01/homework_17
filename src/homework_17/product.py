from homework_17.base_product import BaseProduct
from homework_17.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: int | float,
        quantity: int,
    ) -> None:
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )

    def __add__(self, other) -> int | float:
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа")
        return (
            self.price * self.quantity
            + other.price * other.quantity
        )
