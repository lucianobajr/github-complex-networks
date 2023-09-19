from core.instagram.instagram import Instagram

class InstagramBuilder:
    def __init__(self):
        self.driver = None
        self.username = None
        self.password = None

    def set_driver(self, driver):
        self.driver = driver
        return self

    def set_credentials(self, username, password):
        self.username = username
        self.password = password
        return self

    def build(self) -> Instagram:
        return Instagram(self.driver, self.username, self.password)

