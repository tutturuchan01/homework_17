from homework_17.product import Product


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
