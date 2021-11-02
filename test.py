#TEST 2.3.2
import time
import re
from selenium import webdriver


def getAlertResult(browser):
    alert = browser.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    return result.group(0)    
    
import math  
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.window(browser.window_handles[1])
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_tag_name('input').send_keys(calc(val))
    browser.find_element_by_tag_name('button').click()
    print(getAlertResult(browser))
finally:
    time.sleep(3)
    browser.quit()