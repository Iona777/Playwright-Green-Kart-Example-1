import time

from pytest_bdd import given, when, parsers, then
from conftest import shopping_login_page, shared_data
from pageObjects.shopping_login_page import ShoppingLoginPage
from pageObjects.shopping_dashboard_page import ShoppingDashboardPage

@given('I am on the shopping practice login page')
def navigateToShoppingPage(shopping_login_page: ShoppingLoginPage):
    shopping_login_page.navigateToShoppingLoginPage()

@when('I login to the application')
def loginToShoppingPage(shopping_login_page: ShoppingLoginPage):
    shopping_login_page.loginToShoppingPage("greg.macdonald77@gmail.com", "rsaMania99")

@when(parsers.parse('I add the following items to Cart and checkout {item1}, {item2}'))
def addItemsToCart(shopping_dashboard_page:ShoppingDashboardPage,item1, item2):
    shopping_dashboard_page.select_product(item1)
    shopping_dashboard_page.select_product(item2)

@when('I take note of sum of products')
def takeNoteOfSumOfProducts(shopping_dashboard_page:ShoppingDashboardPage, shared_data):
    shopping_dashboard_page.select_shopping_cart()

    sumOfProducts = shopping_dashboard_page.get_value_of_total()
    # Store sumOfProducts in sharedData so it can be passed around
    shared_data["sumOfProducts"] = sumOfProducts

@when(parsers.parse('I remove {item}'))
def removeGivenItem(shopping_dashboard_page:ShoppingDashboardPage,item):
    shopping_dashboard_page.remove_an_item(item)


@then(parsers.parse('the the new sum of products should be {newSum} than the previous one'))
def checkNewSum(shopping_dashboard_page:ShoppingDashboardPage, newSum, shared_data):
    newTotal = shopping_dashboard_page.get_total_row_value()

    if (newSum == "higher"):
        assert newTotal > shared_data["sumOfProducts"]
        print(f"New Total {newTotal} is higher than old total")
    elif (newSum == "lower"):
        assert newTotal < shared_data["sumOfProducts"]
        print(f"New Total is {newTotal} lower than old total")
    else:
        raise Exception("Invalid value for newSum")

    # For debugging. Remove later
    time.sleep(1)
