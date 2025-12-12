class Common:

    #Like any class in needs a constructor. If we did not need the page class then we would just put 'pass'
    #inside the constructor as it has to have something.
    def __init__(self, page):
        self.page = page


    # Returns the text of the given table, row, column. Zero referenced
    def getNthColumnOfNthRow(self, tableSelector: str, row: int, column: int):
        self.page.wait_for_selector(tableSelector)

        rows = self.page.locator(tableSelector)
        theRow = rows.nth(row)
        text = theRow.locator("td").nth(column).text_content().strip()

        return text