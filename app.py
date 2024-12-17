from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.mozilla.org")
print(driver.title)
driver.quit()
