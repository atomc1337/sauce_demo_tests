import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
def test_add_items_to_cart_with_standard_user(driver):
    base_page_object = BasePage(driver)
    scroll = ActionChains(driver)
    inventory_object = InventoryPage(driver)
    Login.login_with_standard_user(driver)
    inventory_object.add_backpack_to_cart(driver)
    assert base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.DELETE_BACKPACK_ITEM_BUTTON))
    assert base_page_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "1"))
    inventory_object.add_onesie_to_cart(driver)
    assert base_page_object.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "2"))
    assert base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.DELETE_ONESIE_ITEM_BUTTON))

def test_delete_items_from_cart_with_standard_user(driver):
    test_item = BasePage(driver)
    inventory_object = InventoryPage(driver)
    Login.login_with_standard_user(driver)
    inventory_object.add_two_items_to_cart(driver)
    assert test_item.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "2"))
    inventory_object.delete_backpack_from_cart_on_item_block_button(driver)
    assert test_item.wait.until(EC.text_to_be_present_in_element((inventory_object.SHOPPING_CART_BADGE), "1"))
    assert test_item.wait.until(EC.visibility_of_element_located(InventoryPage.ADD_BACKPACK_ITEM_BUTTON))
    inventory_object.delete_onesie_from_cart_on_item_block_button(driver)
    assert test_item.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))
    assert test_item.wait.until(EC.visibility_of_element_located(InventoryPage.ADD_ONESIE_ITEM_BUTTON))


def test_burger_menu_open(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.open_burger_menu_from_inventory_page(driver)
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ALL_ITEMS))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_CLOSE))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_LOGOUT))
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_RESET_APP_STATE))


def test_burger_menu_close(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.open_burger_menu_from_inventory_page(driver)
    assert base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU))
    inventory_object.close_burger_menu_from_inventory_page(driver)
    assert base_page_object.wait.until(EC.invisibility_of_element_located(inventory_object.BURGER_MENU))


def test_click_burger_menu_all_items_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.open_burger_menu_from_inventory_page(driver)
    base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ALL_ITEMS))
    assert driver.current_url == base_page_object.INVENTORY_URL


def test_click_burger_menu_about_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.open_burger_menu_from_inventory_page(driver)
    base_page_object.wait.until(EC.visibility_of_element_located(inventory_object.BURGER_MENU_ABOUT))
    assert driver.current_url == base_page_object.ABOUT_URL


def test_click_burger_menu_logout_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.open_burger_menu_from_inventory_page(driver)
    inventory_object.logout_from_inventory_page_menu(driver)
    assert driver.current_url == base_page_object.LOGIN_URL


def test_click_burger_menu_reset_app_state_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    base_page_object = BasePage(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.add_two_items_to_cart(driver)
    assert base_page_object.wait.until(EC.text_to_be_present_in_element(inventory_object.SHOPPING_CART_BADGE, "2"))
    inventory_object.open_burger_menu_from_inventory_page(driver)
    inventory_object.click_reset_app_state_button(driver)
    assert base_page_object.wait.until(EC.invisibility_of_element_located(inventory_object.SHOPPING_CART_BADGE))


def test_sort_list_items_by_Z_to_A(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_ZA)
    sorted_items = inventory_object.get_inventory_items_names()
    assert sorted_items == sorted(sorted_items, reverse=True)


def test_sort_list_items_by_A_to_Z(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
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
    login_object.login_with_standard_user(driver)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_LOHI)
    sorted_items_lo_to_hi = inventory_object.get_inventory_items_price()
    assert sorted_items_lo_to_hi == sorted(sorted_items_lo_to_hi, reverse=False)


def test_sort_list_items_by_price_hight_to_low(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_LOHI)
    sorted_items_lo_to_hi = inventory_object.get_inventory_items_price()
    assert sorted_items_lo_to_hi == sorted(sorted_items_lo_to_hi, reverse=False)
    inventory_object.click_sort_dropdown()
    inventory_object.sort_option_selector(inventory_object.SORT_OPTION_HILO)
    sorted_items_hi_to_lo = inventory_object.get_inventory_items_price()
    assert sorted_items_hi_to_lo == sorted(sorted_items_hi_to_lo, reverse=True)

def test_open_shopping_cart_from_inventory(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
    assert driver.current_url == inventory_object.INVENTORY_URL
    inventory_object.click_cart_icon_and_go_to_cart()
    assert driver.current_url == inventory_object.CART_URL

def test_go_to_sauce_labs_backpack_cart_from_inventory_on_image(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
    driver.find_element(By.ID, "item_4_img_link").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"


def test_go_to_sauce_labs_backpack_cart_from_inventory_on_name(driver):
    inventory_object = InventoryPage(driver)
    login_object = Login(driver)
    login_object.login_with_standard_user(driver)
    inventory_object.go_to_sauce_labs_backpack()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
