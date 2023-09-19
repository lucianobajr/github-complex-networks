from selenium import webdriver

class DriverManager:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def open_website(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()