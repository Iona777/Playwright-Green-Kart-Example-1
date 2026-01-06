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
        sumOfProdcuts = (self.page.locator("li.totalRow")
                              .filter(has_text="Total").first
                              .locator(".value")
                              .text_content())
        #Strip out the currency symbol and convert to a float.
        sumOfProdcuts = float(sumOfProdcuts.replace("$", ""))

        print(f"SUM OF PRODUCTS IS:  {sumOfProdcuts}")

        return sumOfProdcuts

    def removeAnItem(self, itemToRemove):
        deleteItemButton = (self.page.locator("li.items")
                             .filter(has_text=itemToRemove)
                             .locator("[class='fa fa-trash-o']"))

        deleteItemButton.click()
        #The page does not refresh automatically after clicking the button.
        self.page.reload()

    def getTotalRowValue(self):
        #Gets the 2nd matching element and returns its text value
        totalRowValue = self.page.locator("[class='totalRow'] [class='value']").nth(1).text_content()
        totalRowValue = float( totalRowValue.replace("$", ""))
        print(f"Total value now is: {totalRowValue}")

        return totalRowValue











