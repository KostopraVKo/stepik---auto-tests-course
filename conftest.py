from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def browser():
    print('\nstart chrome')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print('\nquit chrome')
    browser.quit()