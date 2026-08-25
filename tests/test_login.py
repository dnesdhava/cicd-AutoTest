import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config

@pytest.mark.smoke
class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.get_header_title() == "Products"
        assert inventory_page.get_items_count() > 0

    @pytest.mark.regression
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("invalid_user", "invalid_password")

        error_message = login_page.get_error_message_text()
        assert "Username and password do not match" in error_message

    @pytest.mark.regression
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.LOCKED_USER, Config.VALID_PASSWORD)

        error_message = login_page.get_error_message_text()
        assert "Sorry, this user has been locked out" in error_message
