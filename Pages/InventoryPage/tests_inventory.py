import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from Pages.LoginPage.login import Login
from datetime import datetime

def test_add_item_to_card_with_standard_user(driver):
    test_item = BasePage(driver)
    Login.login_with_standard_user(driver)
    button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    button.click()
    assert test_item.wait.until(EC.visibility_of_element_located(((By.ID, "remove-sauce-labs-backpack"))))
    assert test_item.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME, "shopping_cart_badge"))))
    assert test_item.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1"))

