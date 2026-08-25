import pytest
import os
import datetime
from utils.driver_factory import DriverFactory
from utils.logger import get_logger

logger = get_logger("Conftest")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store", default="true", help="Headless execution: true or false")

@pytest.fixture(scope="function")
def driver(request):
    browser_option = request.config.getoption("--browser")
    headless_option = request.config.getoption("--headless").lower() == "true"

    driver_instance = DriverFactory.create_driver(browser=browser_option, headless=headless_option)
    request.node.driver_instance = driver_instance

    yield driver_instance

    logger.info("Tearing down WebDriver session.")
    driver_instance.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call' and report.failed:
        driver_instance = getattr(item, 'driver_instance', None)
        if driver_instance:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver_instance.save_screenshot(file_path)
            logger.error(f"Test failed. Screenshot saved to {file_path}")

            if pytest_html:
                relative_path = os.path.relpath(file_path, os.path.dirname(item.config.option.htmlpath or "."))
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:200px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extras.append(pytest_html.extras.html(html))
    report.extras = extras
