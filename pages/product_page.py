import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_cart_action_product(self):
        self.button_add_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_add_right_product()
        self.should_be_right_cost()

    def add_to_cart(self):
        self.button_add_to_cart()
        self.should_be_add_right_product()
        self.should_be_right_cost()

    def button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add to cart button did not display"
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def should_be_add_right_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text, "Wrong product in cart"

    def should_be_right_cost(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_COST_ALERT).text, "Wrong cost in cart"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_success_massage_after_time(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear after a while"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")