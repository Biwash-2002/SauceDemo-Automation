import pytest

from pages.login_page import LoginPage
from test_data.login_data import LOGIN_TEST_DATA


@pytest.mark.parametrize(
    "username, password, expected_error",
    LOGIN_TEST_DATA
)
def test_invalid_login(page, username, password, expected_error):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert error_message.inner_text() == expected_error


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_empty_username(page):
    login_page = LoginPage(page)

    login_page.open()

    page.locator(login_page.password).fill("secret_sauce")
    page.locator(login_page.login_button).click()

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert error_message.inner_text() == "Epic sadface: Username is required"


def test_empty_password(page):
    login_page = LoginPage(page)

    login_page.open()

    page.locator(login_page.username).fill("standard_user")
    page.locator(login_page.login_button).click()

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert error_message.inner_text() == "Epic sadface: Password is required"


def test_both_fields_empty(page):
    login_page = LoginPage(page)

    login_page.open()

    page.locator(login_page.login_button).click()

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert error_message.inner_text() == "Epic sadface: Username is required"


def test_locked_out_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert error_message.inner_text() == "Epic sadface: Sorry, this user has been locked out."


def test_logout(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"

    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()

    assert page.url == "https://www.saucedemo.com/"