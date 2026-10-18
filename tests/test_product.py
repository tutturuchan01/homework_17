from homework_17.lawn_grass import LawnGrass
from homework_17.product import Product
from homework_17.smartphone import Smartphone


def test_product_initialization():
    product = Product(
        "iPhone",
        "Смартфон Apple",
        100000,
        5,
    )

    assert product.name == "iPhone"
    assert product.description == "Смартфон Apple"
    assert product.price == 100000
    assert product.quantity == 5


def test_new_product():
    product_data = {
        "name": "iPhone",
        "description": "Смартфон Apple",
        "price": 100000,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "iPhone"
    assert product.description == "Смартфон Apple"
    assert product.price == 100000
    assert product.quantity == 5


def test_price_setter():
    product = Product(
        "iPhone",
        "Смартфон Apple",
        100000,
        5,
    )

    product.price = 800

    assert product.price == 800


def test_price_setter_invalid(capsys):
    product = Product(
        "iPhone",
        "Смартфон Apple",
        100000,
        5,
    )

    product.price = -100

    captured = capsys.readouterr()

    assert product.price == 100000
    assert (
        captured.out.strip()
        == "Цена не должна быть нулевая или отрицательная"
    )

    product.price = 0

    captured = capsys.readouterr()

    assert product.price == 100000
    assert (
        captured.out.strip()
        == "Цена не должна быть нулевая или отрицательная"
    )


def test_smartphone_initialization():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "Смартфон Samsung",
        180000,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    assert isinstance(smartphone, Product)
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Газонная трава",
        "Трава для газона",
        500,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert isinstance(grass, Product)
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_product_addition():
    product_1 = Product("iPhone", "Смартфон", 100000, 2)
    product_2 = Product("Samsung", "Смартфон", 80000, 3)

    assert product_1 + product_2 == 440000


def test_smartphone_addition():
    smartphone_1 = Smartphone(
        "Samsung", "Смартфон", 100000, 2,
        95.5, "S23", 256, "Черный",
    )
    smartphone_2 = Smartphone(
        "iPhone", "Смартфон", 120000, 1,
        98.2, "15", 512, "Серый",
    )

    assert smartphone_1 + smartphone_2 == 320000


def test_lawn_grass_addition():
    grass_1 = LawnGrass(
        "Трава 1", "Описание", 500, 2,
        "Россия", "7 дней", "Зеленый",
    )
    grass_2 = LawnGrass(
        "Трава 2", "Описание", 400, 3,
        "США", "5 дней", "Темно-зеленый",
    )

    assert grass_1 + grass_2 == 2200


def test_addition_different_types():
    smartphone = Smartphone(
        "Samsung", "Смартфон", 100000, 2,
        95.5, "S23", 256, "Черный",
    )
    grass = LawnGrass(
        "Трава", "Газонная трава", 500, 20,
        "Россия", "7 дней", "Зеленый",
    )

    try:
        smartphone + grass
    except TypeError:
        assert True
    else:
        assert False, "Ожидалась ошибка TypeError"
