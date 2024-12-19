import unittest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
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

    def add_all_items(self):
        driver = self.driver

        # Adding products to the cart
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            item_button = item.find_element(By.CLASS_NAME, "btn_primary.btn_small.btn_inventory")
            item_button.click()

        # Validating if all items were added
        cart_button = driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()
        cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        cart_badge_val = int(cart_badge.text)
        added = True if cart_badge_val == len(items) else False

        return added

    def fill_checkout_information(self, name="Roberto", last_name="Zepeda", postal_code="45080"):
        driver = self.driver
        # Filling shipping details
        first_name_input = driver.find_element(By.ID, "first-name")
        first_name_input.send_keys(name)
        last_name_input = driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)
        postal_code_input = driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys(postal_code)
        continue_btn = driver.find_element(By.XPATH, '//input[@name="continue"]')
        continue_btn.click()
        try:
            error = self.driver.find_element(By.CLASS_NAME, 'error-message-container')
            return False if error else True
        except NoSuchElementException:
            return True

    def keep_and_delete(self, keep=2):
        driver = self.driver
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        remove = len(cart_items) - keep if len(cart_items) > keep else 0
        for i in range(remove):
            item = cart_items[i]
            item_button = item.find_element(By.CLASS_NAME, "btn.btn_secondary.btn_small.cart_button")
            item_button.click()

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        succeeded = True if  int(len(cart_items)) == keep else False
        return succeeded

    def test_standard_user(self):
        driver = self.driver
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.login.click()

        # Adding products to the cart
        self.add_all_items()
        cart_button = driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()

        # keeping 2 products and deleting the rest
        self.keep_and_delete(1)
        checkout_button = driver.find_element(By.XPATH, '//button[text()="Checkout"]')
        checkout_button.click()

        # Filling shipping details
        information_filled = self.fill_checkout_information()
        if not information_filled:
            self.fail("Checkout information fail. Marking the test as failed.")

        # Finish
        finish_btn = driver.find_element(By.XPATH, '//button[@name="finish"]')
        finish_btn.click()

        # Returning home page
        back_btn = driver.find_element(By.XPATH, '//button[@name="back-to-products"]')
        back_btn.click()

        print("\ntest_standard_user: Test passed successfully!")
        assert True

    def test_problem_user(self):
        driver = self.driver
        self.username.send_keys("problem_user")
        self.password.send_keys("secret_sauce")
        self.login.click()

        # Adding products to the cart
        items_added = self.add_all_items()
        cart_button = driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()

        # keeping 2 products and deleting the rest
        self.keep_and_delete()
        checkout_button = driver.find_element(By.XPATH, '//button[text()="Checkout"]')
        checkout_button.click()

        # Filling shipping details
        information_filled = self.fill_checkout_information()
        if not information_filled:
                self.fail("Checkout information form behavior unexpected.")

        # Finish
        finish_btn = driver.find_element(By.XPATH, '//button[@name="finish"]')
        finish_btn.click()

        # Returning home page
        back_btn = driver.find_element(By.XPATH, '//button[@name="back-to-products"]')
        back_btn.click()

        print("\ntest_problem_user: Test passed successfully!")
        assert True
