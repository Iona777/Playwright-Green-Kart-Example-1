from playwright.sync_api import Page


class Common:
    #Like any class it needs a constructor. If we did not need the page class then we would just put 'pass'
    #inside the constructor as it has to have something.
    def __init__(self, page:Page):
        self.page = page


    # Returns the text of the given table, row, column. Zero referenced
    #Adding '-> str' after the method signature gies the return type. This helps IDE to check that method used correctly.
    def get_nth_column_of_nth_row(self, table_rows_locator: str, row_index: int, col_index: int) -> str:
        #table_rows_locator will be something like "[class='cartTable'] tr"
        #Get all the rows
        rows = self.page.locator(table_rows_locator)
        # Wait for the first element identified by the table__rows_locator to be in a visible state
        rows.first.wait_for(state="visible")

        #Check that row_index is not out of bounds
        if row_index > rows.count():
            raise IndexError(f"Row Index {row_index} out of bounds error. "
                             f"There are only {rows.count()} rows in table")

        #Get a 'pointer' to required row (required as rows is a locator to the rows, not the row elements themselves)
        the_row = rows.nth(row_index)
        #Get all the columns for that required row
        cols = the_row.locator("td")

        if col_index > cols.count():
            raise IndexError(f"Column Index {col_index} out of bounds error."
                             f"There are only {cols.count()} columns in the row")

        #Get a 'pointer' to the required row.
        the_col = cols.nth(col_index)
        #Get the text of the column with whitespace stripped out.
        text = the_col.text_content().strip()

        return text


