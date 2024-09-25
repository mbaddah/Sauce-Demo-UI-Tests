Feature: Filter functionality on SauceDemo
  As a user of the SauceDemo application,
  I want to be able to filter products,
  so that I can quickly find the items I am looking for.

  Background:
    Given I am logged in as a standard user

  Scenario Outline: Successful product filtering
    When I select "<filter_option>" from the filter dropdown
    Then the products should be sorted by "<filter_option>"

    Examples:
      | filter_option       |
      | Name (A to Z)       |
      | Name (Z to A)       |
      | Price (low to high) |
      | Price (high to low) |