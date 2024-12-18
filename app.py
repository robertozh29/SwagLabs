import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        self.login = self.driver.find_element(By.ID, "login-button")

    def tearDown(self):
        self.driver.quit()

    def test_standard_user(self):
        driver = self.driver
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.login.click()

        # Adding products to the cart
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            item_button = item.find_element(By.CLASS_NAME, "btn_primary.btn_small.btn_inventory")
            item_button.click()

        cart_button = driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()

        # Maintaining 2 products and deleting the rest
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        remove = len(cart_items) - 2 if len(cart_items) > 2 else 0
        for i in range(remove):
            item = cart_items[i]
            item_button = item.find_element(By.CLASS_NAME, "btn.btn_secondary.btn_small.cart_button")
            item_button.click()

        checkout_button = driver.find_element(By.XPATH, '//button[text()="Checkout"]')
        checkout_button.click()

        # Filling shipping details
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Roberto")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Zepeda")
        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("45080")
        continue_btn = driver.find_element(By.XPATH, '//input[@name="continue"]')
        continue_btn.click()

        # Finish
        finish_btn = driver.find_element(By.XPATH, '//button[@name="finish"]')
        finish_btn.click()

        # Returning home page
        back_btn = driver.find_element(By.XPATH, '//button[@name="back-to-products"]')
        back_btn.click()

        time.sleep(5)
        assert True

    def _test_problem_user(self):
        driver = self.driver
        self.username.send_keys("problem_user")
        self.password.send_keys("secret_sauce")
        self.login.click()

        assert False

"""
if __name__ == '__main__':
    unittest.main()

input_username = driver.find_element(By.ID, "user-name")
input_username.send_keys(username)
input_password = driver.find_element(By.ID, "password")
input_password.send_keys(password)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

items = driver.find_elements(By.CLASS_NAME, "inventory_item")

for item in items:
    item_button = item.find_element(By.CLASS_NAME, "btn_primary.btn_small.btn_inventory")
    item_button.click()

# driver.quit()
"""