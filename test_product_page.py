from .pages.product_page import ProductPage
import pytest

#@pytest.mark.parametrize('promo_code', range(10))
@pytest.mark.parametrize('promo_code', \
                        [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Page with predefined bug')) \
                        for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_code):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    link = f"{product_base_link}/?promo=offer{promo_code}"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
