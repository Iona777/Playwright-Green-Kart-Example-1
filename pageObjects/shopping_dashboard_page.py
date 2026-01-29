from playwright.sync_api import Page, expect


class ShoppingDashboardPage:
    PRODUCT_CARDS = "[class='card'] [class ='card-body']"
    SHOPPING_CART = "button[routerlink='/dashboard/cart']"
    TOTAL_ROW = "[class='totalRow'] [class='value']"

    def __init__(self, page:Page):
        self.page = page

    @property
    def sum_of_products(self):
        # Can also store complicated locators like this
        return(
            self.page.locator("li.totalRow")
            .filter(has_text="Total").first
            .locator(".value")
        )

    def _parse_currency(self, value: str) -> float:
        return float(value.replace("$", "").strip())

    def select_product(self, productText):
         product = self.page.locator(self.PRODUCT_CARDS).filter(has_text=productText)
         productButton = product.locator("button", has_text="Add To Cart").first
         #If productText is wrong, .first will silently select nothing. Enforce correctness to find errors early
         expect(product).to_have_count(1)
         productButton.click()

    def select_shopping_cart(self):
        #In this case, using the value of routerlink is the most reliable.
        self.page.locator(self.SHOPPING_CART).click()

    def get_value_of_total(self):
        #page.locator("li.totalRow") - this gets all the totalRow elements
        #filter(has_text="Total") - filters on just those that have text "Total", ie. gets rid of the "Subtotal" ones
        #.first returns the first element with text = "Total". Required to avoid Playwright strict‑mode violation,
        #It could be that angular added some hidden duplicate elements.
        #.locator(".value").text_content() - then finds the child element with class containing "Value" and
        #finally returns the text value.

        #This has now been moved to a property at start of class.
        # sumOfProdcuts = (self.page.locator("li.totalRow")Te
        #                       .filter(has_text="Total").first
        #                       .locator(".value")
        #                       .text_content())

        valueOfTotal= self.sum_of_products.text_content()
        #Strip out the currency symbol and convert to a float.
        #valueOfTotal = float(valueOfTotal.replace("$", ""))
        valueOfTotal = self._parse_currency(valueOfTotal)

        print(f"TOTAL VALUE IS:  {valueOfTotal}")

        return valueOfTotal

    #Because of the parameter involved, deleteItemButton locator cannot be a property
    #So, use a method to return the locator. If locator changes, only needs updating on 1 place.
    def get_delete_button(self, itemToRemove):
        deleteItemButton = (self.page.locator("li.items")
                            .filter(has_text=itemToRemove)
                            .locator("[class='fa fa-trash-o']"))

        return deleteItemButton


    def remove_an_item(self, itemToRemove):
        deleteItemButton = self.get_delete_button(itemToRemove)
        deleteItemButton.click()

        #The page does not refresh automatically after clicking the button.
        self.page.reload()

    def get_total_row_value(self):
        #Gets the 2nd matching element and returns its text value
        totalRowValue = self.page.locator(self.TOTAL_ROW).nth(1).text_content()
        #totalRowValue = float( totalRowValue.replace("$", ""))
        totalRowValue = self._parse_currency(totalRowValue)
        print(f"Total value now is: {totalRowValue}")

        return totalRowValue

