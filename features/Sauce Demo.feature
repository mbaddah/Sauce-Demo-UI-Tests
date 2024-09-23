Feature: SauceDemo Application Functionality

  As a user of the SauceDemo application,
  I want to be able to log in, search for products, filter, view product listings, 
  see product details, manage my cart, and complete a checkout process.

  Background:
    Given I am on the SauceDemo login page

  # Log In/Log Out Scenarios
  Scenario: Successful login
    When I enter a valid username and password
    And I click on the "Login" button
    Then I should be redirected to the product listing page
    And I should see a "Logout" option

  Scenario: Unsuccessful login with incorrect credentials
    When I enter an invalid username or password
    And I click on the "Login" button
    Then I should see an error message "Username and password do not match any user in this service"

  Scenario: Log out of the application
    Given I am logged into the SauceDemo application
    When I click on the "Menu" button
    And I click on the "Logout" option
    Then I should be redirected back to the login page

  # Search for Products
  Scenario: Search for a product by name
    Given I am on the product listing page
    When I type "Backpack" into the search bar
    And I press "Enter"
    Then I should see products that contain "Backpack" in the name or description

  # Filtering Products
  Scenario: Filter products by price (low to high)
    Given I am on the product listing page
    When I select "Price (low to high)" from the sort dropdown
    Then I should see products listed in order of price from lowest to highest

  Scenario: Filter products by price (high to low)
    Given I am on the product listing page
    When I select "Price (high to low)" from the sort dropdown
    Then I should see products listed in order of price from highest to lowest

  # Product Listing Page Scenarios
  Scenario: View all available products
    Given I am on the product listing page
    When I load the page
    Then I should see a list of all available products with their names, prices, and images

  Scenario: Add a product to the cart from the product listing page
    Given I am on the product listing page
    When I click the "Add to Cart" button for a product
    Then the product should be added to the cart
    And the cart icon should show the updated number of items

  # Product Details Page Scenarios
  Scenario: View product details
    Given I am on the product listing page
    When I click on a product name or image
    Then I should be redirected to the product details page
    And I should see the product name, image, description, and price

  Scenario: Add a product to the cart from the product details page
    Given I am on the product details page
    When I click the "Add to Cart" button
    Then the product should be added to the cart
    And the cart icon should show the updated number of items

  # Cart Scenarios
  Scenario: View cart with added products
    Given I have added products to my cart
    When I click the "Cart" icon
    Then I should see a list of products in the cart with their quantities and total price

  Scenario: Remove a product from the cart
    Given I have products in my cart
    When I click the "Remove" button next to a product
    Then the product should be removed from the cart
    And the total price should update accordingly

  # Checkout Scenarios
  Scenario: Proceed to checkout
    Given I have products in my cart
    When I click the "Checkout" button
    Then I should be redirected to the checkout information page

  Scenario: Complete the checkout process
    Given I am on the checkout information page
    When I enter my first name, last name, and postal code
    And I click "Continue"
    Then I should be redirected to the order summary page
    And I should see the list of items, total price, and shipping information

  Scenario: Confirm the order
    Given I am on the order summary page
    When I click the "Finish" button
    Then I should see a confirmation message "Thank you for your order"
    And the cart should be empty
