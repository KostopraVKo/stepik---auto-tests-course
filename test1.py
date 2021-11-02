import time
import re
    # webdriver это и есть набор команд для управления браузером
from selenium import webdriver
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Chrome()
    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
#time.sleep(2)
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
'''driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
    # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
    # Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")
    # Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)
    # Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector(".submit-submission")
    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()'''
#ТЕСТ своего сайта
#driver.get("http://127.0.0.1:8000/")
#time.sleep(5)
#wind = driver.find_element_by_css_selector('.block2')
#wind.click()
#time.sleep(5)
#driver.quit()
#ТЕСТ поиск в гугл
'''
driver.get('https://google.com/');
time.sleep(5)
string = driver.find_element_by_css_selector('.gLFyf')
string.send_keys('yandex')
button = driver.find_element_by_css_selector('.gNO89b')
button.click()
time.sleep(5)
driver.quit()'''
#ТЕСТ заполнение формы
'''
link = 'http://suninjuly.github.io/simple_form_find_task.html'
try:
    driver.get(link)
    
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector(".form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(3)
    driver.quit()
'''
#ТЕСТ поиск ссылки на странице - переход по ней - заполнение полей
'''
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_link_text('224592')
    link.click()
    
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(3)
finally:
    browser.quit()
'''
#ТЕСТ - автозаполнение большого количества одинаковых строк
'''
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/huge_form.html')
    link = browser.find_elements_by_tag_name('input')
    print(len(link))
    for i in link:
        i.send_keys('tst')
    butt = browser.find_element_by_css_selector("button.btn")
    butt.click()
    alert = browser.switch_to_alert()
    print(alert.text)
    time.sleep(5)
finally:
    browser.quit()
#'''
#ТЕСТ заполнения строк и выбор определенной кнопки
'''
driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/find_xpath_form'
try:
    driver.get(link)
    
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector(".form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
    alert = driver.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    print(result.group(0))
    time.sleep(1)
finally:
    driver.quit()
#'''

'''browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration2.html'
try:
    browser.get(link)
    inp = browser.find_elements_by_tag_name("input")
    for i in range(3):
        inp[i].send_keys('Gleb')
    time.sleep(2)
    btn = browser.find_element_by_tag_name('button')
    btn.click()
    time.sleep(2)
    message = browser.find_element_by_tag_name('h1').text
    assert message == 'Congratulations! You have successfully registered!'
finally:
    browser.quit()'''
#ТЕСТ на рецензию
'''    
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration2.html'
try:
    browser.get(link)
    inp1 = browser.find_element_by_css_selector(".first_block>.first_class>input")
    inp1.send_keys('name')
    inp1 = browser.find_element_by_css_selector(".first_block>.second_class>input")
    inp1.send_keys('last name')
    inp1 = browser.find_element_by_css_selector(".first_block>.third_class>input")
    inp1.send_keys('email')
    time.sleep(2)
    btn = browser.find_element_by_tag_name('button')
    btn.click()
    time.sleep(2)
    message = browser.find_element_by_tag_name('h1').text
    assert message == 'Congratulations! You have successfully registered!'
finally:
    browser.quit()
    '''
#ТЕСТ 2.1
'''
import math    
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser.get(link)
    value = browser.find_element_by_tag_name('img')
    val = int(value.get_attribute('valuex'))
    inp = browser.find_element_by_id('answer')
    inp.send_keys(calc(val))
    #time.sleep(2)
    cb = browser.find_element_by_id('robotCheckbox')
    cb.click()
    rb = browser.find_element_by_id('robotsRule')
    rb.click()
    time.sleep(3)
    btn = browser.find_element_by_css_selector('[type="submit"]')
    btn.click()
    alert = browser.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    print(result.group(0))
finally:
    time.sleep(5)
    browser.quit()
    '''
 #ТЕСТ 2.2.1
''' 
from selenium.webdriver.support.ui import Select    
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/selects1.html')
    val1 = browser.find_element_by_id('num1').text
    val2 = browser.find_element_by_id('num2').text
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(int(val1) + int(val2)))
    time.sleep(1)
    browser.find_element_by_tag_name('button').click()
finally:
    time.sleep(3)
    browser.quit()
'''
#TEST 2.2.2
'''
import math 
import os   
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser.get(link)
    val = int(browser.find_element_by_id('input_value').text)
    inp = browser.find_element_by_id('answer')
    inp.send_keys(calc(val))
    browser.execute_script('return arguments[0].scrollIntoView(true);', inp)
    #time.sleep(3)
    cb = browser.find_element_by_id('robotCheckbox')
    cb.click()
    rb = browser.find_element_by_id('robotsRule')
    rb.click()
    btn = browser.find_element_by_css_selector('[type="submit"]')
    btn.click()
    alert = browser.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    print(result.group(0))
    #print(os.path.abspath(__file__))
    #print(os.path.abspath(os.path.dirname(__file__)))
finally:
    time.sleep(5)
    browser.quit()'''
#TEST 2.2.3
'''    
import os
browser = webdriver.Chrome()
try:
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)),'txt.txt')
    browser.get('http://suninjuly.github.io/file_input.html')
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Valeriy')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Jmishenko')
    email = browser.find_element_by_name('email')
    email.send_keys('jma@mail.com')
    text = browser.find_element_by_name('file')
    text.send_keys(filename)
    browser.find_element_by_tag_name('button').click()
finally:
    time.sleep(5)
    browser.quit()'''
 #TEST 2.3.1   
'''import math 
import os   
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_tag_name('button').click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_tag_name('input').send_keys(calc(val))
    browser.find_element_by_tag_name('button').click()
finally:
    time.sleep(3)
    browser.quit()'''
#TEST 2.3.2
  
def getAlertResult(browser):
    alert = browser.switch_to_alert()
    result = re.search(r'\d{2}\.\d*$', alert.text)
    return result.group(0)    
    
import math  
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
'''browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_tag_name('button').click()
    #time.sleep(1)
    browser.switch_to.window(browser.window_handles[1])
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_tag_name('input').send_keys(calc(val))
    browser.find_element_by_tag_name('button').click()
    print(getAlertResult(browser))
finally:
    time.sleep(3)
    browser.quit()'''
#EXCAMPLE   
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id('book').click()
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(calc(val))
    browser.find_element_by_id('solve').click()
finally:
    time.sleep(3)
    browser.quit()'''
    
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
    
b = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
try:
    b.get('http://imgpng.ru/')
    #time.sleep(5)
    b.find_element_by_css_selector('[value="Разрешить необходимые"]').click()
    b.find_element_by_name('search').send_keys('assassin')
    #time.sleep(5)
    b.find_element_by_name('search_button').click()
    #time.sleep(5)
    img = b.find_element_by_xpath('//img[@src="http://pngimg.com/uploads/assassins_creed/small/assassins_creed_PNG86.png"]')
    b.execute_script('return arguments[0].scrollIntoView(true);', img)
    #time.sleep(1)
    img.click()
    #time.sleep(5)
    nb = b.windows_handles[3]
    b.switch_to.window(nb)
    #time.sleep(2)
    img = nb.find_element_by_id('lazy-img')
    nb.execute_script('return arguments[0].scrollIntoView(true);', img)
finally:
    time.sleep(5)
    b.quit()
