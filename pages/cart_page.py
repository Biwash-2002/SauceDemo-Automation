from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.backpack_add_button = (
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )

        self.cart_link = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

        self.backpack_item = page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        )

    def add_backpack(self):
        self.click(self.backpack_add_button)

    def open_cart(self):
        self.click(self.cart_link)

    def get_cart_count(self):
        return self.get_text(self.cart_badge)

    def is_backpack_visible(self):
        return self.backpack_item.is_visible()