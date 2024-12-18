from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
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

    def test_problem_user(self):
        driver = self.driver
        self.username.send_keys("problem_user")
        self.password.send_keys("secret_sauce")
        self.login.click()




if __name__ == '__main__':
    unittest.main()
"""
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