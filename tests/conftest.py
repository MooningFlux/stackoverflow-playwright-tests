import pytest
from pages.login_page import LoginPage
from pages.questions_page import QuestionsPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def questions_page(page):
    return QuestionsPage(page)