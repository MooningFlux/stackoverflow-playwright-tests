from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.welcome_message = page.locator("#hide-this-if-you-want h1.fs-headline1")
        self.user_profile_name = page.locator("#user-profile-button span").nth(0) #rebase to base_page?

    def get_welcome_message(self) -> str:
        """Возвращает приветственное сообщение"""
        return self.welcome_message.inner_text()
    
    def get_user_profile_name(self) -> str:
        """Возвращает имя профиля из кнопки юзер профиля"""
        return self.user_profile_name.inner_text()