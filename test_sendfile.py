from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
    input1.send_keys("John")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
    input2.send_keys("Smith")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
    input3.send_keys("test@test.ru")

    file_button = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'testfile.txt')
    file_button.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
