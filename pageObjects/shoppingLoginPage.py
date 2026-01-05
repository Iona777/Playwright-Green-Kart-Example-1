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
        self.sumOfProdcuts = 0

    def navigateToShoppingLoginPage(self):
        self.page.goto(self.baseURL + "client/#/auth/login")

    def loginToShoppingPage(self, email, password):
        self.email.type(email)
        self.password.type(password)
        self.loginButton.click()

    def selectProduct(self, productText):
         product = self.productCards.filter(has_text=productText)
         productButton = product.locator("button", has_text="Add To Cart")
         productButton.click()

    def selectShoppingCart(self):
        #In this case, using the value of routerlink is the most reliable.
        self.page.locator('button[routerlink="/dashboard/cart"]').click()

    def getValueOfTotal(self):
        #page.locator("li.totalRow") - this gets all the totalRow elements
        #filter(has_text="Total") - filters on just those that have text "Total", ie. gets rid of the "Subtotal" ones
        #.first returns the first element with text = "Total". Required to avoid Playwright strict‑mode violation,
        #It could be that angular added some hidden duplicate elements.
        #.locator(".value").text_content() - then finds the child element with class containing "Value" and
        #finally returns the text value.
        self.sumOfProdcuts = (self.page.locator("li.totalRow")
                              .filter(has_text="Total").first
                              .locator(".value")
                              .text_content())
        #Strip out the currency symbol and convert to a float.
        self.sumOfProdcuts = float(self.sumOfProdcuts.replace("$", ""))
        print(f"SUM OF PRODUCTS IS:  {self.sumOfProdcuts}")

    def removeAnItem(self, itemToRemove):
         deleteItemButton = (self.page.locator("li.items")
                             .filter(has_text=itemToRemove)
                             .locator("[class='fa fa-trash-o']"))

         deleteItemButton.click()









