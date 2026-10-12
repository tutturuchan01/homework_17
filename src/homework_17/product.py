class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other) -> int | float:
        if not isinstance(other, Product):
            return NotImplemented
        return (
            self.price * self.quantity
            + other.price * other.quantity
        )
