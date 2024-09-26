from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = '#user-name'
        self.password_input = '#password'
        self.login_button = '#login-button'
        self.error_message = '.error-message-container.error'

    def navigate(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.query_selector(self.error_message).inner_text()