# Selenium test for SwagLabs

This Selenium project is designed to automate browser testing for https://www.saucedemo.com/ using Firefox and Geckodriver for the webdriver and unittest as the testing framework.

## Prerequisites

3. **Python**: Version 3.8 or later
1. **Browser**: Firefox (latest version recommended).
2. **GeckoDriver**: A WebDriver implementation for Firefox.

## Dependencies Installation
**To avoid dependency conflicts, consider using a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Run the script:
1. Navigate to the project directory:
   ```bash
   cd selenium-project/tests
   ```

2. Run a test script using Python:
    ```bash
    python -m unittest app.TestUsers
    ```

## References
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases)