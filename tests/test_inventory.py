import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config

@pytest.mark.regression
class TestInventory:

    @pytest.fixture
    def inventory_page(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)
        return InventoryPage(driver)

    def test_inventory_items_displayed(self, inventory_page):
        assert inventory_page.get_items_count() == 6

    def test_add_item_to_cart(self, inventory_page):
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"

    def test_logout(self, inventory_page, driver):
        inventory_page.logout()
        login_page = LoginPage(driver)
        assert login_page.is_login_button_displayed()
