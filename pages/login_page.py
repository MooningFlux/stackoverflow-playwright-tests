from playwright.sync_api import Page
from pages.base_page import BasePage

# __init__ is basically a function which will "initialize"/"activate" the properties of the class for a specific object, (constructor)
# once created and matched to the corresponding class.
# self represents that object which will inherit those properties.
class LoginPage(BasePage):
    #def __init__(self, page: Page): #mb use locators file with all locators
    def __init__(self, page: Page): #mb use locators file with all locators
        #BasePage.__init__(self, page)
        super().__init__(page)
        #self.page = page
        self.email_input = page.locator('#email')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#submit-button')
        self.error_message = page.get_by_role('paragraph') #The email or password is incorrect.
        #self.error_message = page.locator('#errorAlert')

    def navigate(self):
        """Открывает страницу логина.""" 
        self.page.goto('https://stackoverflow.com/users/login')

    def navigate_tags(self):##delete, make it inherit from base_page. Must be called navigate, and used in tags_page.py
        self.page.goto('https://stackoverflow.com/tags')

    def login(self, email: str, password: str):
        """Выполняет вход с заданными почтой и паролем"""
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
    
    def get_error_message(self):
        """Возвращает текст сообщения об ошибке"""
        return self.error_message.inner_text()