from Pages.LoginPage.login import Login

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
import conftest

def test_login_with_standard_user(driver):
    login_page = Login(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_with_locked_out_user(driver):
    login_page = Login(driver)
    login_page.login("locked_out_user", "secret_sauce")
    exept_block = login_page.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    assert exept_block.text == ("Epic sadface: Sorry, this user has been locked out.")

    login_field = driver.find_element(*Login.USERNAME_INPUT)
    login_field_parent = login_field.find_element(By.XPATH, "./..")
    login_field_parent.find_element(*Login.ERROR_ICON)
    assert "error" in login_field.get_attribute("class")

    password_field = driver.find_element(*Login.USERPASS_INPUT)
    password_field_parent = password_field.find_element(By.XPATH, "./..")
    password_field_parent.find_element(*Login.ERROR_ICON)
    assert "error" in password_field.get_attribute("class")