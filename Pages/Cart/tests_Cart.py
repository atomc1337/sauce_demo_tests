from Pages.ItemCart import ItemCard
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Cart.Cart import Cart
from Pages.ItemCart.ItemCard import ItemCard


def test_click_continue_shopping(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_items_to_cart_and_return_objects()
    inventory_object.click_cart_icon_and_go_to_cart()
    driver.find_element(*cart_object.CONTINUE_SHOPPING).click()
    assert driver.current_url == inventory_object.INVENTORY_URL


def test_delete_item_from_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart = Cart(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_items_to_cart_and_return_objects()
    assert inventory_object.wait.until(EC.text_to_be_present_in_element(inventory_object.SHOPPING_CART_BADGE, "1"))
    inventory_object.click_cart_icon_and_go_to_cart()
    items = cart.get_cart_items()
    #items[0].find_element(*cart.BTN_SECONDARY_REMOVE).click()
    cart.wait.until(EC.visibility_of((items[0].find_element(*cart.BTN_SECONDARY_REMOVE)))).click()
    assert inventory_object.wait.until(EC.invisibility_of_element_located((items[0])))
    assert inventory_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))


def test_go_to_item_page_from_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart = Cart(driver)
    item_card_object = ItemCard(driver)
    login_object.login_with_standard_user(driver)
    inventory_list = inventory_object.add_items_to_cart_and_return_objects()
    id = inventory_object.get_item_id_on_inventory_page(cart.wait.until(EC.visibility_of(inventory_list[0])))
    inventory_object.click_cart_icon_and_go_to_cart()
    items = cart.get_cart_items()
    inventory_object.wait.until(EC.visibility_of((items[0].find_element(*cart.CART_ITEM_NAME)))).click()
    assert driver.current_url == item_card_object.get_item_card_url(id)


def test_click_checkout_on_cart_page(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_items_to_cart_and_return_objects()
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    assert driver.current_url == cart_object.CHECKOUT_STEP_ONE_URL

def test_check_added_item_price_and_name(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart = Cart(driver)
    login_object.login_with_standard_user(driver)
    inv_items = inventory_object.add_items_to_cart_and_return_objects()
    inv_item_price = inv_items[0].find_element(*inventory_object.INVENTORY_ITEM_PRICE).text
    inv_item_name = inv_items[0].find_element(*inventory_object.INVENTORY_ITEM_NAME).text
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_items = cart.get_cart_items()
    cart_item_price = cart_items[0].find_element(*inventory_object.INVENTORY_ITEM_PRICE).text
    cart_item_name = cart_items[0].find_element(*inventory_object.INVENTORY_ITEM_NAME).text
    assert inv_item_price == cart_item_price
    assert inv_item_name == cart_item_name