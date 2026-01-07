

class EcommerceCountryPage:

    def __init__(self, Page):
        self.page = Page
        self.termsAndConditionsCheckbox = self.page.locator("[class='chkAgree']")
        self.proceedButton = self.page.get_by_role("button", name="Proceed")

    def selectCountry(self, country):
        self.page.select_option("div select", country)

    def tickTermsAndConditionsAndProceed(self):
        self.termsAndConditionsCheckbox.check()
        self.proceedButton.click()



