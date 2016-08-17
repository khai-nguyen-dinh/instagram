import time
from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import ProxyType, Proxy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import connect_db


def auto_signup(fullname,email,password,proxy):
    # proxy = Proxy({
    #     'proxyType': ProxyType.MANUAL,
    #     'httpProxy': str(proxy).split(' ')[1],
    #     'ftpProxy': str(proxy).split(' ')[1],
    #     'sslProxy': str(proxy).split(' ')[1],
    #     'noProxy': '45.35.5.232:3362'
    # })
    pr = str(proxy).split(' ')[1]
    display = Display(visible=1, size=(800, 600))
    display.start()
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.NAME, 'email'))
        )
        element_email = driver.find_element_by_name('email')
        element_email.click()
        time.sleep(1)
        element_email.send_keys(email)
        element_fullname = driver.find_element_by_name('fullName')
        element_fullname.click()
        time.sleep(1)
        element_fullname.send_keys(fullname)
        element_password = driver.find_element_by_name('password')
        time.sleep(1)
        element_password.send_keys(password)
        time.sleep(2)
        element_fullname.click()
        time.sleep(2)
        element_password.click()
        time.sleep(2)
        element_username = driver.find_element_by_name('username')
        username = element_username.get_attribute('value')
        element_username.send_keys(Keys.ENTER)
        try:
            WebDriverWait(driver, 15).until(
                EC.title_is('Instagram')
            )
            connect_db.insert_db(fullname,email,username,password,'ok')
        except Exception:
            connect_db.insert_db(fullname, email, username, password, 'error')
    except Exception:
        print ('error!')

