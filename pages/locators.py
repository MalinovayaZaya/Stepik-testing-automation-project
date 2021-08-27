from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//h1[contains(text(),'The shellcoder')]")
    PRODUCT_NAME_ALERT = (By.XPATH, "//strong[contains(text(),'The shellcoder')]")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_COST_ALERT = (By.XPATH, "//strong[contains(text(),'£')]")
