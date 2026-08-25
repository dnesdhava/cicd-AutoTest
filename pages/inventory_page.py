from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_FIRST_ITEM = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_items_count(self) -> int:
        elements = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(elements)

    def add_first_item_to_cart(self) -> None:
        self.js_click(self.ADD_TO_CART_FIRST_ITEM)

    def get_cart_badge_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def logout(self) -> None:
        self.js_click(self.MENU_BUTTON)
        self.js_click(self.LOGOUT_LINK)
