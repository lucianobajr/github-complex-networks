import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Instagram:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        username_elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        
        username_elem.send_keys(self.username)
        password_elem.send_keys(self.password)
        
        submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit.click()

    def handle_notifications(self):
        time.sleep(5)
        try:
            time.sleep(5)
            button = self.driver.find_element(By.CSS_SELECTOR, "div.x1i10hfl")
            button.click()
        except:
            time.sleep(1)

    def turn_off_notifications(self):
        time.sleep(5)
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)")
            button.click()
        except:
            time.sleep(1)