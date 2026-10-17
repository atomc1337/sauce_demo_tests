import time

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
from Pages.CheckoutPartTwo.CheckOutPartTwo import CheckoutPartTwo
def test_click_cancel_button(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_cancel_button()
    assert driver.current_url == checkout_part_two_object.INVENTORY_URL


def test_click_on_item_and_go_to_item_card(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_item_name_and_go_to_item_card()
    assert driver.current_url == checkout_part_two_object.ONSIE_ITEM_URL


def test_click_finish_and_go_to_checkout_complete(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_finish_button()
    assert driver.current_url == checkout_part_two_object.CHECKOUT_COMPLETE_URL
    assert checkout_part_two_object.wait.until(EC.invisibility_of_element_located(checkout_part_two_object.SHOPPING_CART_BADGE))