from playwright.sync_api import Page
from pages.base_page import BasePage

class TagsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        ...


#TODO: assert_ for successful login -> to test files (in po files only actions, locators)