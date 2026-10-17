import time

from Pages.LoginPage.Login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from Pages.helper import Helper
from selenium.webdriver.support.wait import WebDriverWait


# class LoginWith():
def test_login_with_standard_user(driver):
    Login.login_with_standard_user(driver)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_with_locked_out_user(driver):
    login_page = Login(driver)
    Login.login_with_locked_out_user(driver)
    assert login_page.wait.until(EC.visibility_of_element_located(login_page.ERROR_MESSAGE_CONTAINER)).text == (
        "Epic sadface: Sorry, this user has been locked out.")
    assert EC.visibility_of_element_located(Login.USERNAME_ERROR_ICON)
    assert EC.visibility_of_element_located(Login.USERPASS_ERROR_ICON)
    assert login_page.is_field_are_red_with_error(driver) == (True, True)


def test_login_with_problem_user(driver):
    Login.login_with_problem_user(driver)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_with_performance_glitch_user(driver):
    Login.login_with_performance_glitch_user(driver)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_with_error_user(driver):
    Login.login_with_error_user(driver)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_with_visual_user(driver):
    Login.login_with_visual_user(driver)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_without_params(driver):
    test_object = Login(driver)
    button = driver.find_element(*Login.LOGIN_BUTTON)
    button.click()
    assert EC.visibility_of_element_located(Login.USERNAME_ERROR_ICON)
    assert EC.visibility_of_element_located(Login.USERPASS_ERROR_ICON)
    assert EC.text_to_be_present_in_element(Login.ERROR_MESSAGE_CONTAINER, "Epic sadface: Username is required")
    is_fields_are_error = test_object.is_field_are_red_with_error(driver)
    assert is_fields_are_error == (True, True)


def test_close_error_blocks(driver):
    test_object = Login(driver)
    assert test_object.is_field_are_red_with_error(driver) == (False, False)
    test_object.driver.find_element(*Login.LOGIN_BUTTON).click()
    test_object.wait.until(EC.visibility_of_element_located(test_object.ERROR_BUTTON)).click()
    assert EC.invisibility_of_element_located(Login.USERNAME_ERROR_ICON)
    assert EC.invisibility_of_element_located(Login.USERPASS_ERROR_ICON)
    assert EC.invisibility_of_element(Login.ERROR_MESSAGE_CONTAINER)
    is_fields_are_default = test_object.is_field_are_red_with_error(driver)
    assert is_fields_are_default == (False, False)


def test_try_to_login_without_password(driver):
    test_object = Login(driver)
    test_object.login("test_object", "")
    assert test_object.is_field_are_red_with_error(driver) == (True, True)
    assert EC.text_to_be_present_in_element(Login.ERROR_MESSAGE_CONTAINER, "Epic sadface: Password is required")
    assert test_object.driver.find_element(*Login.USERNAME_ERROR_ICON).is_displayed()
    assert test_object.driver.find_element(*Login.USERPASS_ERROR_ICON).is_displayed()


def test_try_to_login_without_username(driver):
    object_of_login = Login(driver)
    object_of_login.login("", "12345")
    assert object_of_login.is_field_are_red_with_error(driver) == (True, True)
    assert EC.text_to_be_present_in_element(Login.ERROR_MESSAGE_CONTAINER, "Epic sadface: Username is required")
    assert object_of_login.driver.find_element(*Login.USERNAME_ERROR_ICON).is_displayed()
    assert object_of_login.driver.find_element(*Login.USERPASS_ERROR_ICON).is_displayed()


def test_try_to_login_on_undefind_user(driver):
    object_of_login = Login(driver)
    object_of_login.login("bad data", "bad data")
    assert object_of_login.is_field_are_red_with_error(driver) == (True, True)
    assert object_of_login.driver.find_element(*object_of_login.USERPASS_ERROR_ICON).is_displayed()
    assert object_of_login.driver.find_element(*object_of_login.USERNAME_ERROR_ICON).is_displayed()
    assert EC.text_to_be_present_in_element(object_of_login.ERROR_MESSAGE_CONTAINER,
                                            "Epic sadface: Username and password do not match any user in this service")


def test_try_to_go_to_inventory_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.INVENTORY_URL)


def test_try_to_go_to_cart_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CART_URL)


def test_try_to_go_to_checkout_step_one_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_STEP_ONE_URL)


def test_try_to_go_to_checkout_step_two_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_STEP_TWO_URL)


def test_try_to_go_to_checkout_complete_without_login(driver):
    object_of_helper = Helper(driver)
    WebDriverWait.until(object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_COMPLETE_URL))

