import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

scenarios('../features/login.feature')


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@given('I am on the SauceDemo login page')
def step_impl(login_page):
    login_page.navigate()

@when(parsers.parse('I enter the username "{username}"'))
def step_impl(login_page, username):
    login_page.page.fill(login_page.username_input, username)

@when(parsers.parse('I enter the password "{password}"'))
def step_impl(login_page, password):
    login_page.page.fill(login_page.password_input, password)

@when('I click the login button')
def step_impl(login_page):
    login_page.page.click(login_page.login_button)

@then('I should see the products page')
def step_impl(inventory_page):
    assert inventory_page.is_loaded()

@then(parsers.parse('I should see the error message "{message}"'))
def step_then(login_page, message):
    error_message = login_page.get_error_message()
    assert message in error_message, f"Expected error message '{message}' not found in '{error_message}'"