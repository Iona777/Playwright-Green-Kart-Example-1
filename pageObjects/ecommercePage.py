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



    def selectAnItem(self,playwright:Playwright ,itemText):
        #Get all the products
        itemLocatorProductClasses = "[class='product-name']"

        products = self.page.locator(itemLocatorProductClasses)
        item = products.get_by_text(itemText)

        # Assert uniqueness
        count = item.count()
        assert count == 1, f"Expected exactly 1 product named '{itemText}', found {count}"

        AddButton = item.get_by_role("Button", name="ADD TO CART")
        AddButton.click()









