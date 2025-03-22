import pytest
import allure
#from pages.login_page import LoginPage
from decouple import config
from tests.conftest import EMAIL, PASSWORD, EMAIL2, PASSWORD2
from playwright.sync_api import expect


def test_create_question(questions_page, authenticated_user): #in real projects - use api for authorization (auth cookies or mocks)
    with allure.step('Перейти на страницу Questions нажатием кнопки'): #by default after authorization user is redirected to /questions page
        questions_page.go_to_questions_page()
    #press ask question button
    with allure.step('Задать корректный вопрос'): #decompose
        questions_page.ask_correct_question()
    questions_page.page.pause()
    #add assert human verification is visible/ this post seems to a duplicate of...


#TODO: #add This post does not meet our quality standards. checking