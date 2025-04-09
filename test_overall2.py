from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

def test_multiple_cart(driver):

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))

    # Add multiple items to the cart
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ]
    for item in items_to_add:
        wait.until(EC.presence_of_element_located((By.ID, item))).click()
    
    # Verify the cart badge shows the correct number of items
    cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == str(len(items_to_add)), "Cart badge does not show the correct number of items"