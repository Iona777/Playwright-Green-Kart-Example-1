from pytest_bdd import given

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





