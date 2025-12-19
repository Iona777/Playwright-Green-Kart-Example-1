Feature: End to end Ecommerce Validation
    Application Regression

    @Regression
    Scenario Outline: Ecommerce products delivery
    Given I open Ecommerce page
    When I add items <item1> and <item2> to Cart
    And I proceed to the checkout
    Then I validate the total prices
    And select the country <country> submit and verify Thank You message
      Examples:
      #Get basic working then add country as a parameter
      |item1      |item2 |country         |
      |Beetroot  |Tomato |India           |
      |Cucumber  |Carrot |United Kingdom  |


    @Smoke
    Scenario Outline: Ecommerce change values on checkout page
        Given I am on the shopping practice login page
      #https://rahulshettyacademy.com/client/#/auth/login
        When I login to the application
      #greg.macdonald77@gmail.com
      #rsaMania99
        And I add the following items to Cart and checkout "<item1>", "<item2>", "<item3>"
        And I take note of sum of products
        And I change the quantity of each item to 3
        And I remove "<item3>"
        Then the the new sum of products should be "<new sum>" than the previous one
        Examples:
            | item1    | item2          | item3      | new sum |
            | iphone X | Samsung Note 8 | Blackberry | higher  |