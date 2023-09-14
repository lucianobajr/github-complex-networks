from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

from config.environments import USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM

browser = webdriver.Chrome("./resources/chromedriver")

browser.get("http://instagram.com")


username = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys(USERNAME_INSTAGRAM)
password.send_keys(PASSWORD_INSTAGRAM)

time.sleep(5)
submit = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

submit.click()

time.sleep(5)
try:
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "div.x1i10hfl")
    button.click()
except:
    time.sleep(1)


# Turn Notifications Off
time.sleep(5)

try:
    button = browser.find_element(
        By.CSS_SELECTOR, "button._a9--:nth-child(2)")
    button.click()
except:
    time.sleep(1)