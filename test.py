from Pages.base_page import BasePage
from conftest import driver
import pdb

object_of_basepage = BasePage(driver)
print(object_of_basepage.CHECKOUT_COMPLETE_URL.split('com', 1)[1])

""""
@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

def login_test(browser):
    browser.get("https://www.saucedemo.com/")
    input_login = browser.find_element(By.ID, "user-name")
    input_login.send_keys("standard_user")
    time.sleep(2)

    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("secret_sauce")
    time.sleep(2)

    ok_button = browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    ok_button.click()
    time.sleep(2)

    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', "url is not valid"
    page_wrapper = browser.find_element(By.CLASS_NAME, 'page_wrapper')
    assert page_wrapper.is_displayed(), 'element not found'

# driver.quit()
"""


def is_happy_number(number):
    l_num = list(str(number))
    half = len(l_num) / 2
    i = 0
    fst_half = []
    snd_half = []
    sqr1 = 1
    sqr2 = 1
    if len(l_num) % 2 != 0:
        return False
    elif len(l_num) % 2 == 0:
        for el in l_num:
            i += 1
            if i > half:
                i = 0
                break
            fst_half.append(el)
            sqr1 = int(el) * sqr1
        pdb.set_trace()
        for el in reversed(l_num):
            i += 1
            if i > half:
                break
            snd_half.append(el)
            sqr2 = int(el) * sqr2
        pdb.set_trace()
        if sqr1 == sqr2:
            return True
        else:
            return False

print(is_happy_number(6262))


str_t = "tet"
int_t = 2
li_t = [2, "tet"]
arr_t = {2, 4, "tet"}


'''def test_try_to_go_to_inventory_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, object_of_helper.INVENTORY_URL)


def test_try_to_go_to_cart_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CART_URL)


def test_try_to_go_to_checkout_step_one_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_STEP_ONE_URL)


def test_try_to_go_to_checkout_step_two_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_STEP_TWO_URL)


def test_try_to_go_to_checkout_complete_without_login(driver):
    object_of_helper = Helper(driver)
    object_of_helper.check_pages_to_go(driver, BasePage.CHECKOUT_COMPLETE_URL)'''