Feature: End to end Ecommerce Validation

  ##NOTE: HAVE ADDED THE OTHER PLAYWRIGHT PROJECT TO TO GIT,BUT NOT THIS ONE YET

    Application Regression
    @Regression
    Scenario: Ecommerce products delivery
    Given I open Ecommerce page
    When I add items to Cart
    And validate the total prices
    Then select the country submit and verify Thank You message

    @Smoke
    Scenario: Filling in the form for the shop
    Given I open Ecommerce page
    When I fill the form details
    |name|gender|
    |bobz|Male|
    Then validate the form behaviour
    And select the shop page

    @Smoke
    Scenario Outline: Filling in the form for the shop- using outline
    Given I open Ecommerce page
    When I fill the form details with name "<name>" and gender "<gender>"
    Then validate the form behaviour
    And select the shop page
    Examples:
    |name|gender|
    |bobz|Male|