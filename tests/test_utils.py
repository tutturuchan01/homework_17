from homework_17.category import Category
from homework_17.utils import load_from_json


def test_load_from_json():
    categories = load_from_json("products.json")

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) > 0
    assert "Samsung Galaxy C23 Ultra" in categories[0].products

    assert categories[1].name == "Телевизоры"
    assert "55\" QLED 4K" in categories[1].products
