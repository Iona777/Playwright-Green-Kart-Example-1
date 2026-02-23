import time

from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers

#from conftest import get_common_class
#You need both the folder name and file name followed by import class name

from pageObjects.ecommerce_country_page import EcommerceCountryPage
from pageObjects.ecommerce_cart_page import EcommerceCartPage
from pageObjects.ecommerce_page import EcommercePage
from utilities.common import Common



@given('I open Ecommerce page')
#Tell it to run the setupBrowserInstance fixture by passing as a parameter
#def open_EcommercePage(setupBrowserInstance, getEcommercePage): might not need this now
def open_ecommerce_page(get_ecommerce_page: EcommercePage):
    #Get page object instance from the getEcommercePage fixture
    get_ecommerce_page.navigateToEcommercePage()


@when(parsers.parse('I add items {item1} and {item2} to Cart'))
#By explicitly annotating the  fixture parameter (getEcommercePage) with the page object type (EcommercePage)
#Then the IDE knows that getEcommercePage is an EcommercePage
#By done the same for item1 and item2 to tell the IDE they are strings, you get prompts for string methods
def add_items_to_cart(get_ecommerce_page: EcommercePage, item1: str, item2:str, ):
    get_ecommerce_page.selectAnItem(item1)
    get_ecommerce_page.selectAnItem(item2)

#Looks like playwright BDD does not recognise 'and' so just use whatever the previous like had
@when('I proceed to the checkout')
def proceed_to_checkout(get_ecommerce_page: EcommercePage):
    get_ecommerce_page.select_basket()
    get_ecommerce_page.proceed_to_checkout()


@then('I validate the total prices')
#Might want to create a different page object for this later
def validate_prices(get_ecommerce_cart_page: EcommerceCartPage, get_common_class: Common):
    #This is just here as an example of how to call a method from the Common class in utilities.common
    #The get_common_class fixture returns an instance of Common in the same way as getEcommercePage returns
    # an instance of the EcommercePage class.
    text =  get_common_class.get_nth_column_of_nth_row("[class='cartTable'] tr", 1, 1)
    print("Text is: "+ text)
    get_ecommerce_cart_page.validate_total_price()


@then(parsers.parse('select the country {country} submit and verify Thank You message'))
#@then('select the country submit and verify Thank You message')
def place_order_and_select_country(get_ecommerce_cart_page: EcommerceCartPage,
                                   get_ecommerce_country_page:EcommerceCountryPage,
                                   country):

    get_ecommerce_cart_page.click_place_order_button()
    get_ecommerce_country_page.selectCountry(country)
    get_ecommerce_country_page.tickTermsAndConditionsAndProceed()

    expect(get_ecommerce_country_page.page.get_by_text("Thank you")).to_be_visible()

    # For debugging. Remove later
    time.sleep(1)








