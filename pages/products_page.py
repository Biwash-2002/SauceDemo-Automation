from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")

    def wait_for_products(self):
        self.product_names.first.wait_for(state="visible")

    def get_product_count(self):
        return self.product_names.count()

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_product_prices(self):
        return self.product_prices.all_inner_texts()