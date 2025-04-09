from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.mark.login
class TestLogin:

    def setup_method(self):
        self.url = "https://www.saucedemo.com/"
        self.username = "standard_user"
        self.password = "secret_sauce"

    def test_successful_login(self, driver):
        driver.get(self.url)
        driver.find_element(By.ID, "user-name").send_keys(self.username)
        driver.find_element(By.ID, "password").send_keys(self.password)
        driver.find_element(By.ID, "login-button").click()
        assert "inventory" in driver.current_url, "Login failed or URL is incorrect"

    def test_invalid_login(self, driver):
        driver.get(self.url)
        driver.find_element(By.ID, "user-name").send_keys(self.username)
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match" in error_message, "Error message not displayed or incorrect"
    
    def test_empty_username(self, driver):
        driver.get(self.url)
        driver.find_element(By.ID, "user-name").send_keys("")
        driver.find_element(By.ID, "password").send_keys(self.password)
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username is required" in error_message, "Error message not displayed or incorrect"
    
    def test_empty_password(self, driver):
        driver.get(self.url)
        driver.find_element(By.ID, "user-name").send_keys(self.username)
        driver.find_element(By.ID, "password").send_keys("")
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Password is required" in error_message, "Error message not displayed or incorrect"
    
    def test_empty_fields(self, driver):
        driver.get(self.url)
        driver.find_element(By.ID, "user-name").send_keys("")
        driver.find_element(By.ID, "password").send_keys("")
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username is required" in error_message, "Error message not displayed or incorrect"