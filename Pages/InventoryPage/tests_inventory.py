import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
import pdb
from Pages.ItemCart.ItemCard import ItemCard
def test_add_items_to_cart_with_standard_user(driver):
    inventory_object = InventoryPage(driver)
    login = Login(driver)
    login.login_with_standard_user()
    first_item = inventory_object.add_items_to_cart_and_return_objects()
    assert first_item[0].find_element(*InventoryPage.BTN_SECONDARY)
    assert inventory_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "1"))
    second_item = inventory_object.add_items_to_cart_and_return_objects()
    assert inventory_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "2"))
    assert second_item[0].find_element(*InventoryPage.BTN_SECONDARY)

def test_delete_items_from_cart_with_standard_user(driver):
    inventory_object = InventoryPage(driver)
    login = Login(driver)
    login.login_with_standard_user()
    list_items = inventory_object.add_items_to_cart_and_return_objects(2)
    assert inventory_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "2"))
    list_items[0].find_element(*inventory_object.BTN_SECONDARY).click()
    assert inventory_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "1"))
    assert inventory_object.wait.until(EC.visibility_of(list_items[0].find_element(*inventory_object.BTN_PRIMARY)))
    inventory_object.wait.until(EC.visibility_of(list_items[1].find_element(*inventory_object.BTN_SECONDARY))).click()
    assert inventory_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))
    assert inventory_object.wait.until(EC.visibility_of(list_items[1].find_element(*inventory_object.BTN_PRIMARY)))


def test_burger_menu_open(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.open_burger_menu_from_inventory_page()
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ALL_ITEMS))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_CLOSE))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_LOGOUT))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_RESET_APP_STATE))


def test_burger_menu_close(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.open_burger_menu_from_inventory_page()
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU))
    inventory_object.close_burger_menu_from_inventory_page()
    assert base_page_object.wait.until(EC.invisibility_of_element_located(inventory_object.BURGER_MENU))


def test_click_burger_menu_all_items_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.open_burger_menu_from_inventory_page()
    base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ALL_ITEMS))
    assert driver.current_url == base_page_object.INVENTORY_URL


def test_click_burger_menu_about_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.open_burger_menu_from_inventory_page()
    base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ABOUT))
    assert driver.current_url == base_page_object.ABOUT_URL


def test_click_burger_menu_logout_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.open_burger_menu_from_inventory_page()
    inventory_object.logout_from_inventory_page_menu()
    assert driver.current_url == base_page_object.LOGIN_URL


def test_click_burger_menu_reset_app_state_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user()
    inventory_object.add_items_to_cart_and_return_objects(2)
    assert base_page_object.wait.until(EC.text_to_be_present_in_element(inventory_object.SHOPPING_CART_BADGE, "2"))
    inventory_object.open_burger_menu_from_inventory_page()
    inventory_object.click_reset_app_state_button()
    assert base_page_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))


def test_sort_list_items_by_Z_to_A(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user()
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_ZA)
    sorted_items = inventory_object.get_inventory_items_names()
    assert sorted_items == sorted(sorted_items, reverse=True)


def test_sort_list_items_by_A_to_Z(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user()
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_ZA)
    sorted_items_z_to_a = inventory_object.get_inventory_items_names()
    assert sorted_items_z_to_a == sorted(sorted_items_z_to_a, reverse=True)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_AZ)
    sorted_items_a_to_z = inventory_object.get_inventory_items_names()
    assert sorted_items_a_to_z == sorted(sorted_items_a_to_z, reverse=False)

def test_sort_list_items_by_price_low_to_hight(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user()
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_LOHI)
    sorted_items_lo_to_hi = inventory_object.get_clean_inventory_items_price(inventory_object.find_items_prices_from_inventory_list())
    assert sorted_items_lo_to_hi == sorted(sorted_items_lo_to_hi, reverse=False)


def test_sort_list_items_by_price_hight_to_low(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user()
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_LOHI)
    sorted_items_lo_to_hi = inventory_object.get_clean_inventory_items_price(inventory_object.find_items_prices_from_inventory_list())
    assert sorted_items_lo_to_hi == sorted(sorted_items_lo_to_hi, reverse=False)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_HILO)
    sorted_items_hi_to_lo = inventory_object.get_clean_inventory_items_price(inventory_object.find_items_prices_from_inventory_list())
    assert sorted_items_hi_to_lo == sorted(sorted_items_hi_to_lo, reverse=True)

def test_open_shopping_cart_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user()
    assert driver.current_url == inventory_object.INVENTORY_URL
    inventory_object.click_cart_icon_and_go_to_cart()
    assert driver.current_url == inventory_object.CART_URL

def test_go_to_item_cart_from_inventory_on_image(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    item_card = ItemCard(driver)
    login_object.login_with_standard_user()
    inventory_list = inventory_object.get_list_items()
    item_id = inventory_object.get_item_id_on_inventory_page(inventory_list[0])
    inventory_list[0].find_element(*inventory_object.INVENTORY_ITEM_IMG).click()
    assert driver.current_url == item_card.get_item_card_url(item_id)


def test_go_to_item_cart_from_inventory_on_name(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    item_card = ItemCard(driver)
    login_object.login_with_standard_user()
    inventory_list = inventory_object.get_list_items()
    item_id = inventory_object.get_item_id_on_inventory_page(inventory_list[0])
    inventory_object.wait.until(EC.visibility_of(inventory_list[0].find_element(*inventory_object.INVENTORY_ITEM_NAME))).click()
    assert driver.current_url == item_card.get_item_card_url(item_id)