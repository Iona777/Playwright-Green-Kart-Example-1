import pytest
from playwright.sync_api import Playwright
from pygments.lexer import default


#Help is optional text to help the user.
#NOTE: make sure you have -- in front of the option name or you will get strange errors.
@pytest.fixture()
def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="Select the browser")


@pytest.fixture
def setupBrowserInstance(playwright:Playwright, request):
    # This will get the option given in the command line.
    browserName = request.config.getoption("browserName")

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
    yield page

    #Teardown
    context.close()
    browser.close()





