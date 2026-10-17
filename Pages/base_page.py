from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    LOGIN_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    CART_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
    CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"
    ONSIE_ITEM_URL = "https://www.saucedemo.com/inventory-item.html?id=2"
    ABOUT_URL = "https://saucelabs.com/about.html"
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    FIRST_NAME = "test_first_name" #Надо убрать креды из base page и вынести в отдельный файл
    LAST_NAME = "test_last_name"
    POSTAL_CODE = "12345"
    ERROR_CLASS = (By.CLASS_NAME, "error")
    ERROR_MESSAGE_CONTAINER = (By.CLASS_NAME, "error-message-container")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")



    def __init__(self, driver: WebDriver, timeout=5):
        self.wait = WebDriverWait(driver, timeout)
        self.driver: WebDriver = driver





