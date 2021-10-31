from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def test_guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
