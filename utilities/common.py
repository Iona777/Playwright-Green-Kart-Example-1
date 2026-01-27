class Common:

    #Like any class in needs a constructor. If we did not need the page class then we would just put 'pass'
    #inside the constructor as it has to have something.
    def __init__(self, page):
        self.page = page


    # Returns the text of the given table, row, column. Zero referenced
    def get_nth_column_of_nth_row(self, table_locator: str, row_index: int, col_index: int):
        self.page.wait_for_selector(table_locator, state="visible")
        rows = self.page.locator(table_locator)
        the_row = rows.nth(row_index)
        cols = the_row.locator("td")
        the_col = cols.nth(col_index)
        text = the_col.text_content().strip()

        return text

