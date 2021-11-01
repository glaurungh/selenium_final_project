from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_should_not_have_any_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items in the basket are presented, but should not be"

    def basket_should_be_empty_basket_text(self):
        assert self.get_empty_basket_message().find("Your basket is empty.") != -1, \
            "Empty basket text isn't presented, but should be"

    def get_empty_basket_message(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text