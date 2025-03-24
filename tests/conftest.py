import pytest
from decouple import config
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.questions_page import QuestionsPage

# @pytest.fixture(scope="module") #session
# def credentials():
#     creds={
#     'EMAIL': config('EMAIL'),
#     'PASSWORD': config('PASSWORD'),
#     'EMAIL2': config('EMAIL2'),
#     'PASSWORD2': config('PASSWORD2')
#     }
#     return creds

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')
EMAIL2 = config('EMAIL2')
PASSWORD2 = config('PASSWORD2')
        

@pytest.fixture(scope="session")
def browser_context_args(browser_name):
    if browser_name == "chromium":
        return {
            "viewport": {
                "width": 1280,
                "height": 720,
            },
            "color_scheme": "dark",
        }
    elif browser_name == "firefox":
        return {
            "viewport": {
                "width": 1366,
                "height": 768,
            },
            "color_scheme": "dark",
        }

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def questions_page(page):
    return QuestionsPage(page)

@pytest.fixture
def authenticated_user(login_page: LoginPage):
    login_page.navigate_login()
    login_page.login(EMAIL2, PASSWORD2)
    #accept cookies, to close the form
    expect(login_page.user_profile_button).to_be_visible()

#add allure-results files deletion