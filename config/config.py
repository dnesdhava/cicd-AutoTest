import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    DEFAULT_BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    EXPLICIT_WAIT_TIMEOUT = int(os.getenv("EXPLICIT_WAIT_TIMEOUT", "10"))
    IMPLICIT_WAIT_TIMEOUT = int(os.getenv("IMPLICIT_WAIT_TIMEOUT", "5"))

    # Credentials for testing
    VALID_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    VALID_PASSWORD = "secret_sauce"
