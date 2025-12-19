from pytest_bdd import given

from pageObjects.shoppingLoginPage import ShoppingLoginPage


@given('I am on the shopping practice login page')
def navigateToShoppingPage(getShoppingLoginPage:ShoppingLoginPage):
    getShoppingLoginPage.navigateToShoppingLoginPage()



