class EcommerceCountryPage:

    def __init__(self, Page):
        self.page = Page
        self.termsAndConditionsCheckbox = self.page.locator("[class='chkAgree']")
        self.proceedButton = self.page.get_by_role("button", name="Proceed")

    #Country is a dropdown which you interact with using select_option(). Pass in the locator of the
    # dropdown and the option to select.
    def selectCountry(self, country):
        self.page.select_option("div select", country)

    def tickTermsAndConditionsAndProceed(self):
        self.termsAndConditionsCheckbox.check()
        self.proceedButton.click()



