import json

from homework_17.category import Category
from homework_17.product import Product


def load_from_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data["products"]:
            product = Product(**product_data)
            products.append(product)

        category = Category(
            category_data["name"],
            category_data["description"],
            products,
        )

        categories.append(category)

    return categories
