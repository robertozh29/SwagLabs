# Unittest for SwagLabs

This README provides the steps and requirements to run an automation testing project for saucedemo.com page.

## Prerequisites

1. **Python**: Ensure Python 3 is installed.
3. **Pip**: Python's package manager for installing dependencies.
4. **Firefox**: A web browser to be automated.
5. **GeckoDriver**: A WebDriver implementation for Firefox.

## Dependencies Installation
**To avoid dependency conflicts, consider using a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Run the script:
```bash
python -m unittest app.TestUsers
```

## References
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases)