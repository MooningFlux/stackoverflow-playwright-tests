from playwright.sync_api import Page
from pages.base_page import BasePage

# __init__ is basically a function which will "initialize"/"activate" the properties of the class for a specific object, (constructor)
# once created and matched to the corresponding class.
# self represents that object which will inherit those properties.
class LoginPage(BasePage):
    def __init__(self, page: Page) -> None: #mb use locators file with all locators
        #BasePage.__init__(self, page)
        super().__init__(page)
        #self.page = page
        self.email_input = page.locator('#email')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#submit-button')
        self.error_message = page.get_by_role('paragraph') #The email or password is incorrect.

    def login(self, email: str, password: str) -> None:
        """Выполнить вход в профиль с заданными почтой и паролем"""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
    
    def get_error_message(self)-> str:
        """Вернуть текст сообщения об ошибке"""
        return self.error_message.inner_text()
    
    