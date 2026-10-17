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
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    driver.find_element(*cart_object.CONTINUE_SHOPPING).click()
    assert driver.current_url == inventory_object.INVENTORY_URL


def test_delete_item_from_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    assert inventory_object.wait.until(EC.text_to_be_present_in_element(inventory_object.SHOPPING_CART_BADGE, "1"))
    inventory_object.click_cart_icon_and_go_to_cart()
    assert inventory_object.wait.until(EC.visibility_of_element_located((Cart.ONESIE_CART)))
    driver.find_element(By.CSS_SELECTOR, "[data-test=remove-sauce-labs-onesie]").click()
    assert inventory_object.wait.until(EC.invisibility_of_element_located((Cart.ONESIE_CART)))
    assert inventory_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))


def test_go_to_onsie_item_page_from_cart(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    item_card_object = ItemCard(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    inventory_object.wait.until(EC.visibility_of_element_located((Cart.ONESIE_CART))).click()
    assert driver.current_url == item_card_object.ONSIE_ITEM_URL


def test_click_checkout_on_cart_page(driver):
    login_object = Login(driver)
    inventory_object = InventoryPage(driver)
    cart_object = Cart(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_onesie_to_cart(driver)
    inventory_object.click_cart_icon_and_go_to_cart()
    cart_object.click_checkout_on_cart_page()
    assert driver.current_url == cart_object.CHECKOUT_STEP_ONE_URL
