from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div.alert.alert-safe.alert-noicon.alert-success")
