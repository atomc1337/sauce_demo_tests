import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Cart.Cart import Cart
from Pages.CheckoutPartOne.CheckoutPartOne import CheckoutPartOne
import pdb


def test_click_cancel(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    cart_object.wait.until(EC.visibility_of_element_located((checkout_part_one_object.CANCEL_BUTTON))).click()
    assert driver.current_url == cart_object.CART_URL


def test_click_continue_with_correct_data(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    assert driver.current_url == checkout_part_one_object.CHECKOUT_STEP_TWO_URL



@pytest.mark.parametrize('user_data',
                         [
                             ('', '', '', "Error: First Name is required"),
                             ('test_first_name', '', '', "Error: Last Name is required"),
                             ('test_first_name', 'test_last_name', '', "Error: Postal Code is required")
                         ]
                         )
def test_click_continue_without_correct_data(driver, user_data):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    first_name, last_name, postal_code, error_message = user_data
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    first_name_field = driver.find_element(*checkout_part_one_object.FIRST_NAME_FIELD)
    first_name_field.send_keys(first_name)
    last_name_field = driver.find_element(*checkout_part_one_object.LAST_NAME_FIELD)
    last_name_field.send_keys(last_name)
    postal_code_field = driver.find_element(*checkout_part_one_object.POSTAL_CODE_FIELD)
    checkout_part_one_object.click_continue_button()
    assert checkout_part_one_object.wait.until(EC.visibility_of_element_located(checkout_part_one_object.ERROR_MESSAGE_CONTAINER)).text == error_message
    assert "error" in first_name_field.get_attribute("class")
    assert "error" in last_name_field.get_attribute("class")
    assert "error" in postal_code_field.get_attribute("class")


def test_close_error_message_by_click_on_xmark(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    error_box = driver.find_element(*checkout_part_one_object.ERROR_MESSAGE_CONTAINER).get_attribute("class").split()
    assert "" not in error_box
    checkout_part_one_object.click_continue_button()
    assert checkout_part_one_object.wait.until(EC.visibility_of_element_located(checkout_part_one_object.ERROR_MESSAGE_CONTAINER))
    assert "error" in driver.find_element(*checkout_part_one_object.FIRST_NAME_FIELD).get_attribute("class")
    checkout_part_one_object.wait.until(EC.visibility_of_element_located(checkout_part_one_object.ERROR_BUTTON)).click()
    assert "" not in error_box
    first_name_classes = driver.find_element(*checkout_part_one_object.FIRST_NAME_FIELD).get_attribute("class").split()
    pdb.set_trace()
    assert "error" not in first_name_classes

