import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright

scenarios('../features/filter.feature')

@pytest.fixture
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page

@given('I am logged in as a standard user')
def login(page):
    page.goto('https://www.saucedemo.com/')
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    assert page.url == 'https://www.saucedemo.com/inventory.html'

@when(parsers.parse('I select "{filter_option}" from the filter dropdown'))
def select_filter_option(page, filter_option):
    filter_dropdown = page.query_selector('.product_sort_container') 
    filter_dropdown.select_option(label=filter_option)

@then(parsers.parse('the products should be sorted by "{filter_option}"'))
def verify_sorted_products(page, filter_option):
    product_elements = page.query_selector_all('.inventory_item')
    product_names = [element.query_selector('.inventory_item_name').inner_text() for element in product_elements]
    product_prices = [float(element.query_selector('.inventory_item_price').inner_text().strip('$')) for element in product_elements]

    if filter_option == 'Name (A to Z)':
        assert product_names == sorted(product_names)
    elif filter_option == 'Name (Z to A)':
        assert product_names == sorted(product_names, reverse=True)
    elif filter_option == 'Price (Low to High)':
        assert product_prices == sorted(product_prices)
    elif filter_option == 'Price (High to Low)':
        assert product_prices == sorted(product_prices, reverse=True)