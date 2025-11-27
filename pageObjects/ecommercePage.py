import time

from playwright.sync_api import Playwright, Page


class EcommercePage:

    #When page instance is created, we will get these parameters passed in
    #By importing Page and including page:Page instead of just page, we will not get a list of available
    # methods for Page.
    def __init__(self,page:Page,baseUrl):
        self.page = page
        self.baseUrl = baseUrl

    def navigateToEcommercePage(self):
        self.page.goto(self.baseUrl + "seleniumPractise/#/")



    def selectAnItem(self,itemText):
        #Get all the products
        #Need to get the product class, not the product-name class as we need to be high enough up
        # the hierarchy for it to also contain te button that we access in a few lines time.
        itemLocatorProductClasses = "[class='product']"
        products = self.page.locator(itemLocatorProductClasses)

        #Now we filter that list on the text of the item we are looking for.
        # We do NOT use item = products.get_by_text(itemText) as this will return the node (element) that
        #contains the text rather than by filtering the list of product elements by the text.
        item = products.filter(has_text=itemText)

        # Assert uniqueness, not sure we really need this, but it is code AI gave.
        count = item.count()
        assert count == 1, f"Expected exactly 1 product named '{itemText}', found {count}"

        #We use the item parent node as starting point for looking for the button
        AddButton = item.get_by_role("button", name="ADD TO CART")
        AddButton.click()

        #For debugging. Remove later
        time.sleep(2)










