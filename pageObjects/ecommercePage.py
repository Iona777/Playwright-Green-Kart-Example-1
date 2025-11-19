class EcommercePage:

    #When page instance is created, we will get these parameters passed in
    def __init__(self,page,baseUrl):
        self.page = page
        self.baseUrl = baseUrl

    def navigateToEcommercePage(self):
        self.page.goto(self.baseUrl + "seleniumPractise/#/")

