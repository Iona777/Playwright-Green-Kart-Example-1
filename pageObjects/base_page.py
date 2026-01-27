from utilities.common import Common

class BasePage:
    def __init__(self, page):
        self.page = page
        self.common = Common(page)
