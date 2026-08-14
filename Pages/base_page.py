from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    LOGIN_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    CART_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    CHECKOUT_STEP_TWO_URL = "https://www.saucedemo.com/checkout-step-two.html"
    CHECKOUT_COMPLETE_URL = "https://www.saucedemo.com/checkout-comlete.html"



    def __init__(self, driver: WebDriver, timeout=5):
        self.wait = WebDriverWait(driver, timeout)
        self.driver: WebDriver = driver





