Feature: SauceDemo Application Functionality

  As a user of the SauceDemo application,
  I want to be able to log in, search for products, filter, view product listings, 
  see product details, manage my cart, and complete a checkout process.

  Background:
    Given I am on the SauceDemo login page

  # Log In/Log Out Scenarios
  # Log In/Log Out Scenarios
    Scenario Outline: Successful login
      When I enter the username "<username>"
      When I enter the password "secret_sauce"
      And I click the login button
      Then I should see the products page

    Examples:
      | username                |
      | standard_user           |
      | locked_out_user         |
      | problem_user            |
      | performance_glitch_user |
      | error_user              |
      | visual_user             |