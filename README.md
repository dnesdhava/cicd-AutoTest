# Selenium Automation Testing Framework

A modular, scalable automated UI testing framework built with **Python**, **Selenium WebDriver**, **pytest**, and the **Page Object Model (POM)** pattern.

---

## 📁 Project Structure

```
cicd-AutoTest/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions CI/CD workflow definition
├── config/
│   └── config.py             # Global configurations & test data
├── utils/
│   ├── driver_factory.py     # Browser driver initialization (Chrome/Firefox, Headless mode)
│   └── logger.py             # Custom logging handler
├── pages/
│   ├── base_page.py          # Base Page class wrapping Selenium interactions & explicit waits
│   ├── login_page.py         # Login Page Objects & Locators
│   └── inventory_page.py     # Inventory/Dashboard Page Objects & Locators
├── tests/
│   ├── test_login.py         # Test cases for login functionality
│   └── test_inventory.py     # Test cases for inventory and cart functionality
├── conftest.py               # Pytest fixtures & HTML report screenshot hooks
├── pytest.ini                # Pytest configuration settings & markers
├── requirements.txt          # Project Python dependencies
└── README.md                 # Documentation
```

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Google Chrome browser installed

### 2. Create Virtual Environment & Install Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests with Specific Browser / Headless Configuration
```bash
# Run Chrome in headless mode (default)
pytest --browser=chrome --headless=true

# Run Chrome with visible UI
pytest --browser=chrome --headless=false
```

### Run Specific Test Suite / Markers
```bash
# Run only smoke tests
pytest -m smoke

# Run only regression tests
pytest -m regression
```

---

## 📊 Test Reports & Logs

- **HTML Report**: Generated automatically after test execution at `reports/report.html`.
- **Logs**: Saved in `logs/test_run_<timestamp>.log`.
- **Failure Screenshots**: Automatically captured and attached to `reports/report.html` and saved in `screenshots/`.

---

## ⚙️ CI/CD Integration

The repository includes a **GitHub Actions** workflow ([`.github/workflows/test.yml`](.github/workflows/test.yml)) configured to run tests automatically on:
- Every push to `main` or `master` branch
- Every pull request
- Scheduled daily run

Test reports and failure screenshots are published as GitHub Artifacts.
