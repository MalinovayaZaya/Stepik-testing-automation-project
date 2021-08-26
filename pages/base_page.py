from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_correct_link(self, substring_url):
        assert substring_url in self.browser.current_url, f"The expected link is not as actual link ('{self.browser.current_url}')"
