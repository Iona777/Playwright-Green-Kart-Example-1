import time
from platform import AndroidVer

from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers

from conftest import getCommonClass
from pageObjects.ecommercePage import EcommercePage
from utilities.common import Common



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

#Looks like playwright BDD does not recognise 'and' so just use whatever the previous like had
@when('I proceed to the checkout')
def proceedToCheckout(getEcommercePage: EcommercePage):
    getEcommercePage.selectBasket()


@then('I validate the total prices')
#Might want to create a different page object for this later
def validatePrices(getEcommercePage: EcommercePage, getCommonClass: Common):


    #This is just here as an example of how to call a method from the Common class in utilities.common
    #The getCommonClass fixture returns an instance of Common in the same way as getEcommercePage returns
    # an instance of the EcommercePage class.
    text =  getCommonClass.getNthColumnOfNthRow("[class='cartTable'] tr",1,1)
    print("Text is: "+ text)

    getEcommercePage.getTotalPrice()
@then(parsers.parse('select the country {country} submit and verify Thank You message'))
#@then('select the country submit and verify Thank You message')
def placeOrderAndSelectCountry(getEcommercePage:EcommercePage, country):
    getEcommercePage.clickPlaceOrderButton()
    getEcommercePage.selectCountry(country)
    getEcommercePage.tickTermsAndConditionsAndProceed()

    expect(getEcommercePage.page.get_by_text("Thank you")).to_be_visible()

    # For debugging. Remove later
    time.sleep(2)








