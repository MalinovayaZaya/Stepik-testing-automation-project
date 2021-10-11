from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")                                       # LOGIN
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")

    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")                    # BASKET


class MainPageLocators():
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")                                 # REGISTER
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIRST_ENTER = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_SECOND_ENTER = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class BasketPageLocators():
    BASKET_PRODUCTS_LIST = (By.CSS_SELECTOR, "div.basket-title")
    BASKET_PRODUCTS_LIST_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#messages")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_NAME = (By.XPATH, "//*[@class='col-sm-6 product_main']//h1")
    PRODUCT_NAME_ALERT = (By.XPATH, "//*[@class='alertinner ']//strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_COST_ALERT = (By.XPATH, "//strong[contains(text(),'£')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-safe")
