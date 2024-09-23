Feature: SauceDemo Application Functionality

  As a user of the SauceDemo application,
  I want to be able to log in, search for products, filter, view product listings, 
  see product details, manage my cart, and complete a checkout process.

  Background:
    Given I am on the SauceDemo login page

  # Log In/Log Out Scenarios
  Scenario: Successful login
    When I enter the username "standard_user"
    When I enter the password "secret_sauce"
    And I click the login button
    Then I should see the products page