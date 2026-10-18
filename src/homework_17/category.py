from homework_17.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только товары")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_info = ""

        for product in self.__products:
            products_info += f"{product}\n"

        return products_info

    def __str__(self) -> str:
        total_quantity = sum(
            product.quantity for product in self.__products
        )
        return (
            f"{self.name}, количество продуктов: "
            f"{total_quantity} шт."
        )
