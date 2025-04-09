from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def test_overall(driver):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Check if the login was successful by verifying the URL
    assert "inventory" in driver.current_url, "Login failed or URL is incorrect"

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1", "Cart badge does not show the correct number of items"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name == "Sauce Labs Backpack", "Item name does not match"

    wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))).click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link"))).click()
    assert "saucedemo" in driver.current_url, "Logout failed or URL is incorrect"


