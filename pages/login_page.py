from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_CONTAINER = (By.ID, "login_button_container")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self) -> None:
        self.open(Config.BASE_URL)

    def login(self, username: str, password: str) -> None:
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_button_displayed(self) -> bool:
        return self.is_displayed(self.LOGIN_BUTTON)
