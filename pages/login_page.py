from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.is_correct_link('login')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_mail.send_keys(email)

        register_password_first_enter = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIRST_ENTER)
        register_password_first_enter.send_keys(password)
        register_password_second_enter = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_SECOND_ENTER)
        register_password_second_enter.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

