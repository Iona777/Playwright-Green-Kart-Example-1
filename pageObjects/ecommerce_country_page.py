class EcommerceCountryPage:

    # Use constants where locators are only strings. Pass as parameters to self.page.locator()
    TERMS_AND_CONDITIONS_TICK_BOX = "[class='chkAgree']"

    def __init__(self, Page):
        self.page = Page
        self.termsAndConditionsCheckbox = self.page.locator("[class='chkAgree']")

    @property
    def proceed_button(self):
        return self.page.get_by_role("button", name="Proceed")

    #Country is a dropdown which you interact with using select_option(). Pass in the locator of the
    # dropdown and the option to select.
    def selectCountry(self, country):
        self.page.select_option("div select", country)

    def tickTermsAndConditionsAndProceed(self):
        self.page.locator(self.TERMS_AND_CONDITIONS_TICK_BOX).click()

        #This uses self.page(), so cannot just be a constant, use property instead
        self.proceed_button.click()



