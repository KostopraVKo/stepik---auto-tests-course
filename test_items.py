import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_interface_language(browser):
    browser.get(link)
    assert browser.find_element_by_xpath('//button[@type="submit"]')
    time.sleep(30)