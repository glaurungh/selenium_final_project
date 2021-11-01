from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "GJgiew832uikgFU&*&bg"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_product_to_basket()
        page.product_name_should_be_in_add_to_basket_messages(product_name)
        page.product_price_should_be_in_add_to_basket_messages(product_price)

@pytest.mark.parametrize('promo_code', range(1))
#@pytest.mark.parametrize('promo_code', range(10))
#@pytest.mark.parametrize('promo_code', \
#                        [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Page with predefined bug')) \
#                        for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_code):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    link = f"{product_base_link}/?promo=offer{promo_code}"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.should_not_be_success_message()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_should_be_in_add_to_basket_messages(product_name)
    page.product_price_should_be_in_add_to_basket_messages(product_price)

@pytest.mark.xfail(reason="Test must fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Not bug but feature")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=1)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_not_have_any_items()
    basket_page.basket_should_be_empty_basket_text()
