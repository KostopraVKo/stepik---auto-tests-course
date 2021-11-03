import time
from selenium import webdriver
    
browser = webdriver.Chrome()
try:
    browser.get('https://dany-pa.github.io/pmtz.github.io/')
    place = browser.find_element_by_css_selector('[placeholder="Задача"]')
    for i in range(1, 101):
        place.send_keys('test number {}'.format(i))
        browser.find_element_by_class_name('btn').click()
        #browser.find_element_by_class_name('btn-success').click()        
finally:
    time.sleep(30)
    browser.quit()