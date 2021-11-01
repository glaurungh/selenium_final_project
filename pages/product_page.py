from .base_page import BasePage
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage):

    def test_guest_can_add_product_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.product_name_should_be_in_add_to_basket_messages(product_name)
        self.product_price_should_be_in_add_to_basket_messages(product_price)

    def product_name_should_be_in_add_to_basket_messages(self, product_name):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name_in_message == product_name, f"Incorrect product name in basket: {product_name_in_message}"

    def product_price_should_be_in_add_to_basket_messages(self, product_price):
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price_in_message == product_price, f"Incorrect product price in basket: {product_price_in_message}"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
