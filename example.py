import time
import re
from selenium import webdriver
    
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getAlertResult(browser):
    alert = browser.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    return result.group(0)    
    
import math  
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id('book').click()
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(val))
    browser.find_element_by_id('solve').click()
    print(getAlertResult(browser))
finally:
    time.sleep(3)
    browser.quit()