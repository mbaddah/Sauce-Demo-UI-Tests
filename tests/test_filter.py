import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios('../features/filter.feature')

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@given('I am logged in as a standard user')
def login(login_page, inventory_page):
    login_page.navigate()
    login_page.login('standard_user', 'secret_sauce')
    assert inventory_page.is_loaded()

@when(parsers.parse('I select "{filter_option}" from the filter dropdown'))
def select_filter_option(inventory_page, filter_option):
    inventory_page.select_filter_option(filter_option)

@then(parsers.parse('the products should be sorted by "{filter_option}"'))
def verify_sorted_products(inventory_page, filter_option):
    product_names = inventory_page.get_product_names()
    product_prices = inventory_page.get_product_prices()

    if filter_option == 'Name (A to Z)':
        assert product_names == sorted(product_names)
    elif filter_option == 'Name (Z to A)':
        assert product_names == sorted(product_names, reverse=True)
    elif filter_option == 'Price (Low to High)':
        assert product_prices == sorted(product_prices)
    elif filter_option == 'Price (High to Low)':
        assert product_prices == sorted(product_prices, reverse=True)