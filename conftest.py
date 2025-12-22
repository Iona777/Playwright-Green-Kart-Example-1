import pytest
from playwright.sync_api import Playwright
from collections import namedtuple
from pageObjects.ecommercePage import EcommercePage
from pageObjects.shoppingLoginPage import ShoppingLoginPage
from utilities.common import  Common

#This is a list the Python module paths to of all your stepDef files.
#Each string like "stepDefs.loginPageStepDef" refers to a Python module that is
#located in a package called stepDefs and has a file named loginPageStepDefs. py
#inside it.
#Make sure that steDefs is a proper Python package, i.e. it as an
# __init__.py file, which can be blank.

pytest_plugins = [
    "stepDefs.ecommercePageStepDef",
    "stepDefs.shoppingPageStepDef"

]

#Makes this available for sharing data throughout the current scenario, if required.
scenario_context = {}


#Help is optional text to help the user.
#NOTE: make sure you have -- in front of the option name or you will get strange errors.
def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="Select the browser")
    parser.addoption("--baseUrl", action="store", default="https://rahulshettyacademy.com/", help="Set baseUrl")

#This is like setting up your driver.
@pytest.fixture
def setupBrowserInstance(playwright:Playwright, request):

    # This will get the option given in the command line.
    browserName = request.config.getoption("browserName")
    baseUrl = request.config.getoption("baseUrl")

    if(browserName == "chrome"):
        browser = playwright.chromium.launch(headless=False)
    elif (browserName == "firefox"):
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browserName}")
        
    context = browser.new_context()
    page = context.new_page()

    # This will return the page then it will stop (give way, yield) until the calling test completes.
    # Then it will run any steps that are after this line. In this way it performs tearDown steps.
    # Yield both page and baseUrl so that baseUrl can be set from command line for different environments

    # This makes it easier to access the individual parts of BrowserInstance
    BrowserInstance = namedtuple("BrowserInstance", ["page", "baseUrl"])

    yield BrowserInstance(page,baseUrl)

    #Teardown
    context.close()
    browser.close()

    # run from terminal like this:
    # pytest test_testFileName.py --browser_name chrome
    # or like this if passing in base_url too
    # pytest test_testFileName.py - -browser_name chrome --base_url https: // rahulshettyacademy.com


@pytest.fixture
#Calls the EcommercePage constructor and returns an instance of the page object.
#This constructor also needs the baseURL which is local to the setupBrowserInstance() method.
# So, create a class variable dictionary,scenario_context, and pass the data around that way
def getEcommercePage(setupBrowserInstance):
    localBrowserInstance = setupBrowserInstance
    return EcommercePage(localBrowserInstance.page, localBrowserInstance.baseUrl)

#Calls the Common constructor and returns an instance of the Common class.
@pytest.fixture
def getCommonClass(setupBrowserInstance):
    localBrowserInstance = setupBrowserInstance
    return  Common(localBrowserInstance.page)

#Add similar for the other pages as required.
@pytest.fixture()
def getShoppingLoginPage(setupBrowserInstance):
    localBrowserInstance = setupBrowserInstance
    return ShoppingLoginPage(localBrowserInstance.page, localBrowserInstance.baseUrl)







