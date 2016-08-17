import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





driver = webdriver.PhantomJS()
driver.get("https://www.instagram.com/")
try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.NAME, 'email'))
    )
    element_email = driver.find_element_by_name('email')
    print element_email
    element_email.send_keys('khainguyenptiter+kai@gmail.com')
    element_fullname = driver.find_element_by_name('fullName')
    element_fullname.send_keys('khai nguyen dinh')
    element_password = driver.find_element_by_name('password')
    element_password.send_keys('adgjmptw95')
    element_username = driver.find_element_by_name('username')
    element_username.send_keys('khainguyen112233')
    element_username.send_keys(Keys.ENTER)
    WebDriverWait(driver, 15).until(
        EC.title_is('instagram')
    )
except Exception as e:
    print e