from playwright.sync_api import Playwright, Page, expect, Locator


class EcommercePage:
    #When page instance is created, we will get these parameters passed in
    #By importing Page and including page:Page instead of just page, we will not get a list of available
    # methods for Page.

    BASKET_ICON = "[class='cart-icon']"
    ITEM_LOCATOR_PRODUCT_CLASSES = "[class='product']"

    def __init__(self, page: Page):
        self.page = page

    @property
    def proceed_to_checkout_icon(self):
        return self.page.get_by_role("button", name="PROCEED TO CHECKOUT")


    def navigateToEcommercePage(self):
        self.page.goto("seleniumPractise/#/")

    def selectAnItem(self, itemText):
        #Get all the products
        #Need to get the product class, not the product-name class as we need to be high enough up
        # the hierarchy for it to also contain te button that we access in a few lines time.
        products = self.page.locator(self.ITEM_LOCATOR_PRODUCT_CLASSES)
        print("Type of products is ", type(products))

        #Now we filter that list on the text of the item we are looking for.
        # We do NOT use item = products.get_by_text(itemText) as this will return the node (element) that
        #contains the text rather than by filtering the list of product elements by the text.
        item = products.filter(has_text=itemText)
        print("Type of item is ", type(item))

        # Assert uniqueness, not sure why we really need this, but it is code AI gave.
        count = item.count()
        assert count == 1, f"Expected exactly 1 product named '{itemText}', found {count}"

        #We use the item parent node as starting point for looking for the button
        AddButton = item.get_by_role("button", name="ADD TO CART")
        AddButton.click()

    def select_basket(self):
        #Using the locators defined at top of class, similar to Selenium style POM. Else use properties.
        self.page.locator(self.BASKET_ICON).click()

    def proceed_to_checkout(self):
        self.proceed_to_checkout_icon.click()


