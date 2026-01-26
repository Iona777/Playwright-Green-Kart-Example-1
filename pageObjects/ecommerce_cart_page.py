from playwright.sync_api import Page

#Class names need to start in upper case or python gets mixed up
class EcommerceCartPage:

    def __init__(self,page: Page):
        self.page = page
        #Better to define locators in constructor so a available to all methods in page object
        self.displayedTotalPrice = self.page.locator("[class='totAmt']")
        self.placeOrderButton = self.page.get_by_role("button", name="Place Order")

    def getTotalPrice(self):
        #Wait for the table to be rendered. While Playwright will for elements to be ready before
        # interacting with them, getting the count does not qualify as interaction, so it does not wait
        # automatically. Setting state="visible" is stricter than the default which only checks for the
        #element to be attached to the DOM.
        self.page.wait_for_selector("[class='cartTable'] tr", state="visible")


        #How to get the contents of nth row of a table:
        #Find all the rows in the given table and store in a variable, e.g. 'rows'
        #Get a count of how many rows there are in
        #Use a for loop in the form
        #for i in range(1,count): # skip header row
        #Get the current row using rows.nth(i) and store in a variable, e.g. 'theRow'
        #Get the text of the current row using
        #text = theRow.locator("td").nth(n).text_content().strip(), where n is the number of the column you want.

        #To answer in an interview:
        #Get all the rows in the given table
        #Loop round them using rows.nth(i) as a pointer to the current row
        #Use  locator("td").nth() on current row to get its contents.

        rows = self.page.locator("[class='cartTable'] tr")
        count = rows.count()
        print(f"Number of rows, including header, is {count}")

        print(f"rows is type {type(rows)}")

        calculated_totalPrice = 0

        #Can't use 'for item in rows' as rows is a selector, not a list.
        #This is equivalent of for i=1 to count;i++
        for i in range(1, count):  # skip header row
            #get the 3rd column value
            theRow = rows.nth(i)
            price_text = theRow.locator("td").nth(3).text_content().strip()
            print(f"Column text is {price_text}")
            #Need to convert from a string to a number
            price = float(price_text)
            calculated_totalPrice = calculated_totalPrice + price

            print(f"Total price is {calculated_totalPrice}")

        displayedTotalPrice_text = self.displayedTotalPrice.text_content().strip()

        #If the text contained a currency symbol, then you could strip it out like this:
        #displayedTotalPrice_text = displayedTotalPrice_text.replace("£", "").strip()

        #Need to convert to float so can use as a number
        displayedTotalPriceValue = float(displayedTotalPrice_text)

        print(f"Calculated total price is {calculated_totalPrice} and displayed total prices is {displayedTotalPriceValue}")
        assert calculated_totalPrice == displayedTotalPriceValue, \
            (f"Displayed total {displayedTotalPriceValue} does not match calculated {calculated_totalPrice}")

    def clickPlaceOrderButton(self):
        self.placeOrderButton.click()
