from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_link = ".shopping_cart_link"
        self.checkout_button = "[data-test='checkout']"

        self.first_name = "[data-test='firstName']"
        self.last_name = "[data-test='lastName']"
        self.postal_code = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"

        self.finish_button = "[data-test='finish']"
        self.error_message = "[data-test='error']"

        self.thank_you_message = page.locator(
            ".complete-header"
        )

        self.backpack_add_button = (
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )

    def add_backpack_and_open_checkout(self):

        self.click(self.backpack_add_button)

        self.click(self.cart_link)

        self.click(self.checkout_button)

    def fill_checkout_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.postal_code, postal_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_error_visible(self):
        return self.is_visible(self.error_message)

    def is_thank_you_visible(self):
        self.thank_you_message.wait_for(
            state="visible",
            timeout=10000
        )
        return self.thank_you_message.is_visible()