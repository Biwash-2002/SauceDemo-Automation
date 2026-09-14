from playwright.sync_api import Page

from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open(self):
        self.open_url(BASE_URL)

    def login(self, username, password):
        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_error_visible(self):
        return self.is_visible(self.error_message)