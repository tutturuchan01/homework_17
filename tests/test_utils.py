from homework_17.category import Category
from homework_17.product import Product
from homework_17.utils import load_from_json


def test_load_from_json():
    categories = load_from_json("products.json")

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products[0], Product)

    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3

    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
