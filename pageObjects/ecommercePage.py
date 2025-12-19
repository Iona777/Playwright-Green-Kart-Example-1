import time

from playwright.sync_api import Playwright, Page, expect, Locator


class EcommercePage:
    #When page instance is created, we will get these parameters passed in
    #By importing Page and including page:Page instead of just page, we will not get a list of available
    # methods for Page.

    def __init__(self, page: Page, baseUrl):
        self.page = page
        self.baseUrl = baseUrl
        #Locators
        self.basketIcon = self.page.locator("[class='cart-icon']")
        self.proceedToCheckoutIcon = self.page.get_by_role("button", name="PROCEED TO CHECKOUT")
        self.placeOrderButton = self.page.get_by_role("button", name="Place Order")
        self.termsAndConditionsCheckbox  = self.page.locator("[class='chkAgree']")
        self.proceedButton = self.page.get_by_role("button", name="Proceed")

    def navigateToEcommercePage(self):
        self.page.goto(self.baseUrl + "seleniumPractise/#/")

    def selectAnItem(self, itemText):
        #Get all the products
        #Need to get the product class, not the product-name class as we need to be high enough up
        # the hierarchy for it to also contain te button that we access in a few lines time.
        itemLocatorProductClasses = "[class='product']"
        products = self.page.locator(itemLocatorProductClasses)
        print("Type of products is ", type(products))

        #Now we filter that list on the text of the item we are looking for.
        # We do NOT use item = products.get_by_text(itemText) as this will return the node (element) that
        #contains the text rather than by filtering the list of product elements by the text.
        item = products.filter(has_text=itemText)
        print("Type of item is ", type(item))

        # Assert uniqueness, not sure we really need this, but it is code AI gave.
        count = item.count()
        assert count == 1, f"Expected exactly 1 product named '{itemText}', found {count}"

        #We use the item parent node as starting point for looking for the button
        AddButton = item.get_by_role("button", name="ADD TO CART")
        AddButton.click()

    def selectBasket(self):
        #Using the locators defined in the constructor, similar to Selenium style POM
        self.basketIcon.click()
        self.proceedToCheckoutIcon.click()

    def getTotalPrice(self):
        #Wait for the table to be rendered. While Playwright will for elements to be ready before
        # interacting with them, getting the count does not qualify as interaction, so it does not wait automatically.
        self.page.wait_for_selector("[class='cartTable'] tr")

        #How to get the contents of nth row of a table:
        #Find all the rows in the given table and store in a variable, e.g. 'rows'
        #Get a count of how many rows there are in
        #Use a for loop in the form
        #for i in range(1,count): # skip header row
        #Get the current row using rows.nth(i) and store in a variable, e.g. 'theRow'
        #Get the text of the current row using
        #text = theRow.locator("td").nth(n).text_content().strip(), where n is the number of the column you want.

        #To answer in an interview:
        #Get al the rows in the given table
        #Loop round them using rows.nth(i) as a pointer to the current row
        #Use  locator("td").nth() on current row to get its contents.

        rows = self.page.locator("[class='cartTable'] tr")
        count = rows.count()
        print(f"Number of rows, including header, is {count}")

        print(f"rows is type {type(rows)}")

        totalPrice = 0

        #Can't use 'for item in rows' as rows is a selector, not a list.
        #This is equivalent of for i=1 to count;i++
        for i in range(1, count):  # skip header row
            #get the 3rd column value
            theRow = rows.nth(i)
            price_text = theRow.locator("td").nth(3).text_content().strip()
            print(f"Column text is {price_text}")
            #Need to convert from a string to a number
            price = float(price_text)
            totalPrice = totalPrice + price

            print(f"Total price is {totalPrice}")

        displayedTotalPrice_text = self.page.locator("[class='totAmt']").text_content().strip()

        #If the text contained a currency symbol, then you could strip it out like this:
        #displayedTotalPrice_text = displayedTotalPrice_text.replace("£", "").strip()

        displayedTotalPrice = float(displayedTotalPrice_text)

        print(f"Calculated total price is {totalPrice} and displayed total prices is {displayedTotalPrice}")
        assert totalPrice == displayedTotalPrice, \
            (f"Displayed total {displayedTotalPrice} does not match calculated {totalPrice}")

    def clickPlaceOrderButton(self):
        self.placeOrderButton.click()

    def selectCountry(self, country):
        self.page.select_option("div select", country)

    def tickTermsAndConditionsAndProceed(self):
        self.termsAndConditionsCheckbox.check()
        self.proceedButton.click()
