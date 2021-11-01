from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        eml = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        eml.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1_FIELD)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2_FIELD)
        pass2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login") != -1, "Substring 'login' wasn't found in the url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
