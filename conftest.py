import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: Сhrome or Firefox"
    )
    parser.addoption(
        "--browser_language",
        action="store",
        default="en",
        help="Choose language: ru, en, ..., (etc.)"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    browser_language = request.config.getoption("browser_language").lower()

    if browser_name == "chrome":
        print("\n\nStart Chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\n\nStart Firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        # raise pytest.UsageError("--browser_name should be chrome or firefox") # если мы хотим кинуть ошибку
        print(f"\nWhoops! {browser_name} browser is not supported. Starting Chrome instead")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    yield browser
    print("\nQuit browser...")
    browser.quit()