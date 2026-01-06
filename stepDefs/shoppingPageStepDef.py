import time
from sys import exception

from pytest_bdd import given, when, parsers, then

from conftest import getShoppingLoginPage, sharedData
from pageObjects.shoppingLoginPage import ShoppingLoginPage

@given('I am on the shopping practice login page')
def navigateToShoppingPage(getShoppingLoginPage:ShoppingLoginPage):
    getShoppingLoginPage.navigateToShoppingLoginPage()

@when('I login to the application')
def loginToShoppingPage(getShoppingLoginPage:ShoppingLoginPage):
    getShoppingLoginPage.loginToShoppingPage("greg.macdonald77@gmail.com","rsaMania99")

@when(parsers.parse('I add the following items to Cart and checkout {item1}, {item2}'))
def addItemsToCart(getShoppingLoginPage:ShoppingLoginPage,item1, item2):
    getShoppingLoginPage.selectProduct(item1)
    getShoppingLoginPage.selectProduct(item2)

@when('I take note of sum of products')
def takeNoteOfSumOfProducts(getShoppingLoginPage,sharedData):
    getShoppingLoginPage.selectShoppingCart()
    sumOfProducts = getShoppingLoginPage.getValueOfTotal()
    # Store sumOfProducts in sharedData so it can be passed around
    sharedData["sumOfProducts"] = sumOfProducts

@when(parsers.parse('I remove {item2}'))
def removeGivenItem(getShoppingLoginPage,item2):
    getShoppingLoginPage.removeAnItem(item2)


@then(parsers.parse('the the new sum of products should be {newSum} than the previous one'))
def checkNewSum(getShoppingLoginPage, newSum, sharedData):
    newTotal = getShoppingLoginPage.getTotalRowValue()


    print(f"Old total was: {sharedData["sumOfProducts"]}")

    print(f"New total is {newTotal}")


    if (newSum == "higher"):
        assert newTotal > sharedData["sumOfProducts"]
        print(f"New Total is higher than old total")
    elif (newSum == "lower"):
        assert  newTotal < sharedData["sumOfProducts"]
        print(f"New Total is lower than old total")
    else:
        raise Exception("Invalid value for newSum")


    # For debugging. Remove later
    time.sleep(5)






