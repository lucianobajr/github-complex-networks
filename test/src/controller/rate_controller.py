import instaloader

from exceptions.custom_exception import CustomException

class MyRateController(instaloader.RateController):
    def __init__(self, context):
        super().__init__(context)
        self.context = context

    def sleep(self, secs):
        raise CustomException()