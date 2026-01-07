Feature: End to end Ecommerce Validation
    Application Regression

    @Regression
    Scenario Outline: Ecommerce products delivery
      #ecommerce page
    Given I open Ecommerce page
    When I add items <item1> and <item2> to Cart
    And I proceed to the checkout
      #cart page
    Then I validate the total prices
      #cart page and country page
    And select the country <country> submit and verify Thank You message
      Examples:
      #Get basic working then add country as a parameter
      |item1      |item2 |country         |
      |Beetroot  |Tomato |India           |
      |Cucumber  |Carrot |United Kingdom  |


    @Smoke
    Scenario Outline: Ecommerce shopping page, change values on checkout page
      #login page
        Given I am on the shopping practice login page
        When I login to the application
      #dashboard page
        And I add the following items to Cart and checkout <item1>, <item2>
        And I take note of sum of products
        And I remove <item2>
        Then the the new sum of products should be <newSum> than the previous one
        Examples:
            | item1         | item2           |  newSum  |
            | ZARA COAT 3   | ADIDAS ORIGINAL |  lower    |