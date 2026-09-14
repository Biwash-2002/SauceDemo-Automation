from pages.cart_page import CartPage


def test_add_product_to_cart(logged_in_page):
    page = logged_in_page

    cart_page = CartPage(page)

    cart_page.add_backpack()

    assert page.locator(cart_page.cart_badge).is_visible()
    assert cart_page.get_cart_count() == "1"


def test_product_appears_in_cart(logged_in_page):
    cart_page = CartPage(logged_in_page)

    cart_page.add_backpack()
    cart_page.open_cart()

    assert cart_page.is_backpack_visible()