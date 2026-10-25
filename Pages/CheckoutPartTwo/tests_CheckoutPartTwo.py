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
from Pages.ItemCart.ItemCard import ItemCard
def test_click_cancel_button(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user()
    inventory_object.add_items_to_cart_and_return_objects()
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_cancel_button()
    assert driver.current_url == checkout_part_two_object.INVENTORY_URL


def test_click_on_item_and_go_to_item_card(driver):
    item_cart = ItemCard(driver)
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user()
    item = inventory_object.add_items_to_cart_and_return_objects()
    item_id = inventory_object.get_item_id_on_inventory_page(item[0])
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_item_name_and_go_to_item_card()
    assert driver.current_url == item_cart.get_item_card_url(item_id)


def test_click_finish_and_go_to_checkout_complete(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    login_object.login_with_standard_user()
    inventory_object.add_items_to_cart_and_return_objects()
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    checkout_part_two_object = CheckoutPartTwo(driver)
    checkout_part_two_object.click_finish_button()
    assert driver.current_url == checkout_part_two_object.CHECKOUT_COMPLETE_URL
    assert checkout_part_two_object.wait.until(EC.invisibility_of_element_located(checkout_part_two_object.SHOPPING_CART_BADGE))
    assert checkout_part_two_object.wait.until(EC.text_to_be_present_in_element(checkout_part_two_object.COMPLETE_HEADER, "Thank you for your order!"))

def test_check_item_name_price(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    checkout_part_two = CheckoutPartTwo(driver)
    login_object.login_with_standard_user()
    added_items = inventory_object.add_items_to_cart_and_return_objects()
    item_price_inv = inventory_object.get_clean_inventory_items_price(added_items[0].find_element(*inventory_object.INVENTORY_ITEM_PRICE))
    item_name_inv = added_items[0].find_element(*inventory_object.INVENTORY_ITEM_NAME).text
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    chk2_items = checkout_part_two.get_cart_items()
    item_price_chk2 = checkout_part_two.get_clean_items_price(chk2_items[0].find_element(*checkout_part_two.ITEM_PRICE))
    item_name_chk2 = chk2_items[0].find_element(*checkout_part_two.ITEM_NAME).text
    assert item_name_inv == item_name_chk2
    assert item_price_inv == item_price_chk2


def test_check_total_price_tax_and_final_price(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    checkout_part_one_object = CheckoutPartOne(driver)
    checkout_part_two = CheckoutPartTwo(driver)
    login_object.login_with_standard_user()
    added_items = inventory_object.add_items_to_cart_and_return_objects()
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    checkout_part_one_object.click_continue_with_correct_data_on_name_lname_postal()
    chk2_items = checkout_part_two.get_cart_items()
    chk2_items_prices = checkout_part_two.get_clean_items_price_total(chk2_items)
    chk2_prices_summ = checkout_part_two.items_price_summ(chk2_items_prices)
    #pdb.set_trace()
    assert checkout_part_two.get_sum() == chk2_prices_summ
    assert checkout_part_two.get_clean_items_tax(chk2_prices_summ) == checkout_part_two.get_tax()
    assert checkout_part_two.get_total_price_final() == checkout_part_two.get_tax() + checkout_part_two.get_sum()

