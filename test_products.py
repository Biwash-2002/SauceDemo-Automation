from pages.products_page import ProductsPage

def test_products_page_loads(logged_in_page):
    page = logged_in_page

    products_page = ProductsPage(page)

    assert page.url == "https://www.saucedemo.com/inventory.html"

    products_page.wait_for_products()

    assert products_page.get_product_count() == 6

def test_product_count(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.wait_for_products()

    assert products_page.get_product_count() == 6


def test_product_names(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.wait_for_products()

    expected_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]

    assert products_page.get_product_names() == expected_names


def test_product_prices(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.wait_for_products()

    expected_prices = [
        "$29.99",
        "$9.99",
        "$15.99",
        "$49.99",
        "$7.99",
        "$15.99"
    ]

    assert products_page.get_product_prices() == expected_prices