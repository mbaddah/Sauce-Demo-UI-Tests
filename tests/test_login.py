import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright

scenarios('../features/login.feature')

# @pytest.fixture
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@given('I am on the SauceDemo login page')
def step_impl(page):
    page.goto('https://www.saucedemo.com/')

@when(parsers.parse('I enter the username "{username}"'))
def step_impl(page, username):
    page.fill('#user-name', username)


@when(parsers.parse('I enter the password "{password}"'))
def step_impl(page, password):
    page.fill('#password', password)

@when('I click the login button')
def step_impl(page):
    page.click('#login-button')

@then('I should see the products page')
def step_impl(page):
    assert "Products" in page.content()