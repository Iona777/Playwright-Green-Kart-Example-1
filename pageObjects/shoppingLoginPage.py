from playwright.sync_api import Page


class ShoppingLoginPage:

    def __init__(self, page:Page, baseURL):
        self.page = Page
        self.baseURL = baseURL
        self.email = page.locator('#userEmail')
        self.password = page.locator('#userPassword')
        self.loginButton = page.locator("[class ='btn btn-block login-btn']")

    def navigateToShoppingLoginPage(self):
        self.page.goto(self.baseURL + "client/#/auth/login")

    def loginToShoppingPage(self, email, password):
        self.email.type(email)
        self.password.type(password)
        self.loginButton.click()








