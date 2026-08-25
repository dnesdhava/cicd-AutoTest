from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config
from utils.logger import get_logger

logger = get_logger("DriverFactory")

class DriverFactory:
    @staticmethod
    def create_driver(browser: str = None, headless: bool = None) -> webdriver.Remote:
        browser_name = (browser or Config.DEFAULT_BROWSER).lower()
        is_headless = headless if headless is not None else Config.HEADLESS

        logger.info(f"Initializing WebDriver: browser={browser_name}, headless={is_headless}")

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if is_headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if is_headless:
                options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        driver.maximize_window()
        return driver
