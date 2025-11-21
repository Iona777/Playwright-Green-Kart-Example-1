Feature: End to end Ecommerce Validation
    Application Regression

    @Regression
    Scenario Outline: Ecommerce products delivery
    Given I open Ecommerce page
    When I add items <item1> and <item2> to Cart
    And validate the total prices
    Then select the country submit and verify Thank You message
      Examples:
      |item1      |item2 |
      |Beetroot  |Tomato |



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