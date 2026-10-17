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
from Pages.CheckoutComplete.CheckoutComlete import CheckoutComplete
def test_click_go_to_home_button(driver):
    checkout_complete_object = CheckoutComplete(driver)
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
    checkout_complete_object.click_back_home()
    assert driver.current_url == checkout_complete_object.INVENTORY_URL

"""def test_click_generate_pdf_order(driver):
    checkout_complete_object = CheckoutComplete(driver)
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
    checkout_complete_object.click_generate_pdf_order()
    assert """
