from pytest_bdd import given, when, parsers

from conftest import setupBrowserInstance
from pageObjects.ecommercePage import EcommercePage


@given('I open Ecommerce page')
#Tell it to run the setupBrowserInstance fixture by passing as a parameter
def open_EcommercePage(setupBrowserInstance):
    #setupBrowserInstance yields both page and baseURL
    page, baseURL = setupBrowserInstance

    #Create page object instance, it takes both page and baseURL as parameters
    ecommercePage = EcommercePage(page, baseURL)
    ecommercePage.navigateToEcommercePage()

    #Could look into putting ecommercePage into sharedDate or similar so we do not need to keep recreating it

@when(parsers.parse('I add items {item1} and {item2} to Cart'))


#@when(parsers.parse( 'I login to the portal with {username} and {password}'))
def addItemsToCart(item1, item2,setupBrowserInstance):
    #setupBrowserInstance will yield BrowserInstance(page,baseUrl)
    # which is a named tuple containing page and baseUrl.
    BrowserInstance = setupBrowserInstance
    page = BrowserInstance.page
    baseURl = BrowserInstance.baseUrl

    ecommercePage = EcommercePage(page, baseURl)
    ecommercePage.selectAnItem(item1)
    ecommercePage.selectAnItem(item2)














