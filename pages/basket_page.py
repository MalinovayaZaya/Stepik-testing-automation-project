from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        self.is_correct_link('basket')

    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_PRODUCTS_LIST), "Basket is not empty"

    def should_be_empty_basket_massage(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PRODUCTS_LIST_EMPTY_MESSAGE), \
            "Basket empty message is not displayed"
