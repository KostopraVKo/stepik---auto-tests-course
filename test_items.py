import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_xpath('//button[@type="submit"]')
    time.sleep(30)