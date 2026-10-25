import pdb
import time

import pytest

from Pages.LoginPage.Login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize(
    'user_and_pass',
    [
        ('standard_user', "secret_sauce"),
        ('problem_user', "secret_sauce"),
        ('performance_glitch_user', "secret_sauce"),
        ('error_user', "secret_sauce"),
        ('visual_user', "secret_sauce")
    ]
)
def test_login_with_some_users(driver, user_and_pass):
    login = Login(driver)
    user, password = user_and_pass
    login.login(user, password)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize(
    'user_pass_error',
    [
        ('locked_out_user', "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ('', "", "Epic sadface: Username is required"),
        ('error_user', "", "Epic sadface: Password is required"),
        ('', "secret_sauce", "Epic sadface: Username is required"),
        ('bad data', "bad data", "Epic sadface: Username and password do not match any user in this service")
    ]
)
def test_try_to_login_with_bad_data(driver, user_pass_error):
    login = Login(driver)
    user, password, error = user_pass_error
    login.login(user, password)
    assert driver.current_url == "https://www.saucedemo.com/"
    assert login.wait.until(EC.visibility_of_element_located(login.ERROR_MESSAGE_CONTAINER)).text == error
    assert EC.visibility_of_element_located(Login.USERNAME_ERROR_ICON)
    assert EC.visibility_of_element_located(Login.USERPASS_ERROR_ICON)
    assert login.is_field_are_red_with_error(driver) == (True, True)


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


@pytest.mark.parametrize(
    'url', [
        "https://www.saucedemo.com/inventory.html",
        "https://www.saucedemo.com/cart.html",
        "https://www.saucedemo.com/checkout-step-one.html",
        "https://www.saucedemo.com/checkout-step-two.html",
        "https://www.saucedemo.com/checkout-complete.html",
    ]
)
def test_try_to_go_to_pages_without_login(driver, url):
    login = Login(driver)
    login.wait_for_page_to_load()
    login.driver.get(url)
    endpoint_to_message = (url.split('.com', 1)[1])
    assert login.wait.until(EC.url_contains("https://www.saucedemo.com/"))
    assert login.is_field_are_red_with_error(driver) == (True, True)
    assert login.wait.until(EC.text_to_be_present_in_element(login.ERROR_MESSAGE_CONTAINER, f"Epic sadface: You can only access '{endpoint_to_message}' when you are logged in."))
    assert login.driver.find_element(*login.USERNAME_ERROR_ICON).is_displayed()
    assert login.driver.find_element(*login.USERPASS_ERROR_ICON).is_displayed()

