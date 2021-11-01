from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

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
    page.test_guest_can_add_product_to_basket()

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
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()