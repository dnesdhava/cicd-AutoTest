import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from config.config import Config
from utils.logger import get_logger

logger = get_logger("BasePage")

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT_TIMEOUT)

    def open(self, url: str) -> None:
        logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        logger.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def js_click(self, locator: tuple[str, str]) -> None:
        logger.info(f"JS Clicking element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        logger.info(f"Entering text into element: {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        logger.info(f"Retrieved text from {locator}: '{text}'")
        return text

    def is_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            return False

    def get_title(self) -> str:
        title = self.driver.title
        logger.info(f"Page title: '{title}'")
        return title

    def take_screenshot(self, name: str) -> str:
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        path = os.path.join(screenshots_dir, f"{name}.png")
        self.driver.save_screenshot(path)
        logger.info(f"Saved screenshot to {path}")
        return path
