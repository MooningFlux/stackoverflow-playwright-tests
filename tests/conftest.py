import pytest
from decouple import config
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.tags_page import TagsPage
from pages.questions_page import QuestionsPage
from playwright.sync_api import Page, APIResponse
from _pytest.fixtures import FixtureRequest

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

KEY = "rl_bDjukFK2wQnvjqrqBVhCHDEWp"

#consider storage
PROBLEM_DESCRIPTION = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

EXPECTED_RESULT = """
Sed ut perspiciatis unde omnis iste natus error sit voluptatem
accusantium doloremque laudantium, totam rem aperiam...
"""        

@pytest.fixture(scope="session")
def browser_context_args(browser_name):
    if browser_name == "chromium":
        return {
            "viewport": {
                "width": 1366,
                "height": 768,
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
def home_page(page):
    return HomePage(page)

@pytest.fixture
def tags_page(page):
    return TagsPage(page)

@pytest.fixture
def questions_page(page):
    return QuestionsPage(page)

@pytest.fixture
def authenticated_user(login_page: LoginPage) -> None:
    login_page.navigate_login()
    login_page.login(EMAIL2, PASSWORD2)
    #accept cookies, to close the form
    expect(login_page.user_profile_button).to_be_visible()

@pytest.fixture #with parameter in request obj
def api_question_response(page: Page, request: FixtureRequest) -> APIResponse: #no need to explicitly annotate
    #Запрашиваем response вопроса через API с указанным id
    question_id = request.param  # Получаем ID из параметризации
    response = page.request.get(
        f"https://api.stackexchange.com/2.3/questions/{question_id}",
        params={"site": "stackoverflow"}
    )
    assert response.status == 200 #.ok
    return response

#delete
@pytest.fixture
def api_question_4_response(questions_page: QuestionsPage) -> APIResponse:
    #Запрашиваем данные вопроса через API с указанным id
        response = questions_page.page.request.get(
            "https://api.stackexchange.com/2.3/questions/4",
            params={"site": "stackoverflow"}
        )
        assert response.status == 200
        return response

#add allure-results files deletion