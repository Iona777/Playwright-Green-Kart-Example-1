import time

from pytest_bdd import given, when, parsers

from pageObjects.shoppingLoginPage import ShoppingLoginPage


@given('I am on the shopping practice login page')
def navigateToShoppingPage(getShoppingLoginPage:ShoppingLoginPage):
    getShoppingLoginPage.navigateToShoppingLoginPage()

@when('I login to the application')
def loginToShoppingPage(getShoppingLoginPage:ShoppingLoginPage):
    getShoppingLoginPage.loginToShoppingPage("greg.macdonald77@gmail.com","rsaMania99")

#@when(parsers.parse('I add the following items to Cart and checkout {item1}, {item2}, {item3}'))
@when(parsers.parse('I add the following items to Cart and checkout {item1}, {item2}'))
def addItemsToCart(getShoppingLoginPage:ShoppingLoginPage,item1, item2):
    getShoppingLoginPage.selectProduct(item1)
    getShoppingLoginPage.selectProduct(item2)
    
    # For debugging. Remove later
    time.sleep(5)






