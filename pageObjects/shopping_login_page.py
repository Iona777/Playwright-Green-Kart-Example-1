from playwright.sync_api import Page


class ShoppingLoginPage:

    def __init__(self, page:Page, baseURL):
        #Make sure you set self.page = page, not Page (i.e. the instance not the class) or you will get odd problems.
        self.page = page
        self.baseURL = baseURL
        self.email = page.locator('#userEmail')
        self.password = page.locator('#userPassword')
        self.loginButton = page.locator("[class ='btn btn-block login-btn']")

        self.productCards = page.locator("[class='card'] [class ='card-body']")
        #Can also store complicated locators like this
        self.sumOfProducts = (
            self.page.locator("li.totalRow")
            .filter(has_text="Total").first
            .locator(".value")
        )

    def navigateToShoppingLoginPage(self):
        self.page.goto(self.baseURL + "client/#/auth/login")

    def loginToShoppingPage(self, email, password):
        self.email.type(email)
        self.password.type(password)
        self.loginButton.click()










