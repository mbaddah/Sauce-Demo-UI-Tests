Feature: Cart functionality on SauceDemo
  As a user of the SauceDemo application,
  I want to be able to add and remove products from the cart,
  so that I can manage my shopping list.

  Background:
    Given I am logged in as a standard user

  @skip
  Scenario: Add a product to the cart
    When I add the product "Sauce Labs Backpack" to the cart
    Then the cart should contain "1" item

  @skip
  Scenario: Remove a product from the cart
    Given I have added the product "Sauce Labs Backpack" to the cart
    When I remove the product "Sauce Labs Backpack" from the cart
    Then the cart should be empty