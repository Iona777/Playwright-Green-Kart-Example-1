import time

from pytest_bdd import given, when, parsers
from pageObjects.ecommercePage import EcommercePage


@given('I open Ecommerce page')
#Tell it to run the setupBrowserInstance fixture by passing as a parameter
#def open_EcommercePage(setupBrowserInstance, getEcommercePage): might not need this now
def open_EcommercePage(getEcommercePage: EcommercePage):
    #Get page object instance from the getEcommercePage fixture
    getEcommercePage.navigateToEcommercePage()


@when(parsers.parse('I add items {item1} and {item2} to Cart'))
#By explicitly annotating the  fixture parameter (getEcommercePage) with the page object type (EcommercePage)
#Then the IDE knows that getEcommercePage is an EcommercePage
#By done the same for item1 and item2 to tell the IDE they are strings, you get prompts for string methods
def addItemsToCart(item1: str, item2:str, getEcommercePage: EcommercePage):
    getEcommercePage.selectAnItem(item1)
    getEcommercePage.selectAnItem(item2)
