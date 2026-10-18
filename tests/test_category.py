from homework_17.category import Category
from homework_17.product import Product
from homework_17.smartphone import Smartphone


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
    assert category.products == "iPhone, 100000 руб. Остаток: 5 шт.\n"


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


def test_add_product():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Техника", [])

    product = Product("iPhone", "Смартфон", 100000, 5)

    result = category.add_product(product)

    assert result is None
    assert Category.product_count == 1
    assert category.products == "iPhone, 100000 руб. Остаток: 5 шт.\n"


def test_add_smartphone():
    Category.product_count = 0

    category = Category("Смартфоны", "Техника", [])
    smartphone = Smartphone(
        "Samsung", "Смартфон", 100000, 2,
        95.5, "S23", 256, "Черный",
    )

    category.add_product(smartphone)

    assert Category.product_count == 1
    assert "Samsung" in category.products


def test_add_invalid_product():
    category = Category("Смартфоны", "Техника", [])

    try:
        category.add_product("Not a product")
    except TypeError:
        assert True
    else:
        assert False, "Ожидалась ошибка TypeError"
