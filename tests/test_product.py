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
