from pages.checkout_page import CheckoutPage


def test_checkout_page_loads(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    assert page.url == "https://www.saucedemo.com/checkout-step-one.html"


def test_checkout_information(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    checkout_page.fill_checkout_information(
        "Biwash",
        "Thapa",
        "44600"
    )

    checkout_page.continue_checkout()

    assert page.url == "https://www.saucedemo.com/checkout-step-two.html"


def test_complete_checkout(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    checkout_page.fill_checkout_information(
        "Biwash",
        "Thapa",
        "44600"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert page.url == "https://www.saucedemo.com/checkout-complete.html"
    assert checkout_page.is_thank_you_visible()


def test_checkout_empty_first_name(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    checkout_page.fill_checkout_information(
        "",
        "Thapa",
        "44600"
    )

    checkout_page.continue_checkout()

    assert checkout_page.is_error_visible()
    assert "First Name is required" in checkout_page.get_error_message()


def test_checkout_empty_last_name(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    checkout_page.fill_checkout_information(
        "Biwash",
        "",
        "44600"
    )

    checkout_page.continue_checkout()

    assert checkout_page.is_error_visible()
    assert "Last Name is required" in checkout_page.get_error_message()


def test_checkout_empty_postal_code(logged_in_page):
    page = logged_in_page

    checkout_page = CheckoutPage(page)

    checkout_page.add_backpack_and_open_checkout()

    checkout_page.fill_checkout_information(
        "Biwash",
        "Thapa",
        ""
    )

    checkout_page.continue_checkout()

    assert checkout_page.is_error_visible()
    assert "Postal Code is required" in checkout_page.get_error_message()