from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_to_alert = browser.find_element(By.TAG_NAME, "button")
    button_to_alert.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    button_submit = browser.find_element(By.TAG_NAME, "button")
    button_submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
