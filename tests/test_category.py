from homework_17.category import Category
from homework_17.product import Product


def test_category_initialization():
    product = Product(
        "iPhone",
        "Смартфон Apple",
        100000,
        5,
    )

    category = Category(
        "Электроника",
        "Электронные устройства",
        [product],
    )

    assert category.name == "Электроника"
    assert category.description == "Электронные устройства"
    assert category.products == [product]


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    Category("Электроника", "Техника", [])

    assert Category.category_count == 1


def test_product_count():
    Category.category_count = 0
    Category.product_count = 0

    product_1 = Product("iPhone", "Смартфон", 100000, 5)
    product_2 = Product("ASUS", "Ноутбук", 150000, 3)

    Category(
        "Электроника",
        "Техника",
        [product_1, product_2],
    )

    assert Category.product_count == 2
