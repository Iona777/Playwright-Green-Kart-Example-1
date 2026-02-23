from playwright.sync_api import Page


class ShoppingLoginPage:
    EMAIL = "#userEmail"
    PASSWORD = "#userPassword"
    LOGIN_BUTTON = "[class ='btn btn-block login-btn']"
    PRODUCT_CARDS = "[class='card'] [class ='card-body']"

    def __init__(self, page:Page):
        #Make sure you set self.page = page, not Page (i.e. the instance not the class) or you will get odd problems.
        self.page = page

    def navigateToShoppingLoginPage(self):
        self.page.goto("client/#/auth/login")

    def loginToShoppingPage(self, email, password):
        self.page.locator(self.EMAIL).type(email)
        self.page.locator(self.PASSWORD).type(password)
        self.page.locator(self.LOGIN_BUTTON).click()













