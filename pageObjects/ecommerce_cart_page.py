from playwright.sync_api import Page
from pageObjects.base_page import BasePage


#Class names need to start in upper case or python gets mixed up
class EcommerceCartPage(BasePage):
    #Use constants where locators are only strings. Pass as parameters to self.page.locator()
    CART_TABLE = "[class='cartTable'] tr"
    DISPLAYED_TOTAL_PRICE = "[class='totAmt']"
    PLACE_ORDER_NAME = "Place Order"

    def __init__(self,page: Page):
        #Don't technically need a constructor here as it inherits one from BasePage.
        #However, if I ever need to add more lines to this constructor then I will need both this
        # and super(). This future proofs this.
        super().__init__(page)

    #Use properties where the locator is more complicated and needs self.page. This will return a locator,
    # so don't need to use self.page() again when using this.
    @property
    def place_order_button(self):
        return self.page.get_by_role("button", name=self.PLACE_ORDER_NAME)


    #Although the tests do not really need it, here is an example of how to call a method from the
    # common clas within a page object. The BasePage class calls the constructor fo Common class and
    # makes it available to any page objects that inherit from BasePage
    def get_first_item_price(self):
        return self.common.get_nth_column_of_nth_row(
            self.CART_TABLE,
            row_index=1,
            col_index=1
        )

    def validate_total_price(self):
        #Wait for the table to be rendered. While Playwright will wait for elements to be ready before
        # interacting with them, getting the count does not qualify as interaction, so it does not wait
        # automatically. Setting state="visible" is stricter than the default which only checks for the
        #element to be attached to the DOM.
        self.page.wait_for_selector(self.CART_TABLE, state="visible")


        #How to get the contents of nth row of a table:
        #Find all the rows in the given table and store in a variable, e.g. 'rows'
        #Get a count of how many rows there are.
        #Use a for loop in the form
        #for i in range(1,count): # skip header row
        #Get the current row using rows.nth(i) and store in a variable, e.g. 'theRow'
        #Get the text of the current row using
        #text = theRow.locator("td").nth(n).text_content().strip(), where n is the number of the column you want.

        #To answer in an interview:
        #Get all the rows in the given table
        #Loop round them using rows.nth(i) as a pointer to the current row
        #Use  locator("td").nth() on current row to get its contents.

        rows = self.page.locator(self.CART_TABLE)
        count = rows.count()

        calculated_total_price = 0

        #Can't use 'for item in rows' as rows is a selector, not a list.
        #This is equivalent of for i=1 to count;i++
        for i in range(1, count):  # skip header row
            #get the 3rd column value
            the_row = rows.nth(i)
            price_text = the_row.locator("td").nth(3).text_content().strip()
            print(f"Column text is {price_text}")
            #Need to convert from a string to a number
            price = float(price_text)
            calculated_total_price = calculated_total_price + price

        displayed_total_price_text = self.page.locator(self.DISPLAYED_TOTAL_PRICE).text_content().strip()

        #If the text contained a currency symbol, then you could strip it out like this:
        #displayedTotalPrice_text = displayedTotalPrice_text.replace("£", "").strip()

        #Need to convert to float so can use as a number
        displayed_total_price_value = float(displayed_total_price_text)

        assert calculated_total_price == displayed_total_price_value, \
            (f"Displayed total {displayed_total_price_value} does not match calculated {calculated_total_price}")

    def click_place_order_button(self):
        self.place_order_button.click()
