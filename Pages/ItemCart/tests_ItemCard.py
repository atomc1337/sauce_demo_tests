from Pages.ItemCart.ItemCard import ItemCard
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_inventory_by_arrow(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    item_card_object = ItemCard(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.go_to_sauce_labs_backpack()
    driver.find_element(*item_card_object.BACK_TO_PRODUCTS).click()
    assert driver.current_url == inventory_object.INVENTORY_URL

def test_add_sauce_labs_backpack_from_item_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.go_to_sauce_labs_backpack()
    item_card_object = ItemCard(driver)
    driver.find_element(*item_card_object.ADD_TO_CARD).click()
    assert inventory_object.wait.until(EC.text_to_be_present_in_element(inventory_object.SHOPPING_CART_BADGE, "1"))

def test_remove_sauce_labs_backpack_from_item_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.go_to_sauce_labs_backpack()
    item_card_object = ItemCard(driver)
    driver.find_element(*item_card_object.ADD_TO_CARD).click()
    inventory_object.wait.until(EC.visibility_of_element_located((item_card_object.REMOVE))).click()
    assert inventory_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))

def test_go_to_cart_from_item(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.go_to_sauce_labs_backpack()
    driver.find_element(*inventory_object.SHOPPING_CART_LINK).click()
    assert driver.current_url == inventory_object.CART_URL

