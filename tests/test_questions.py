import pytest
import allure
from playwright.sync_api import expect
from pages.questions_page import StackOverflowAPI

@pytest.mark.xfail
def test_create_duplicate_question(questions_page, authenticated_user):
    with allure.step('Перейти на страницу Questions нажатием кнопки'):
        questions_page.go_to_questions_page()
    with allure.step('Задать корректный вопрос'):
        questions_page.ask_correct_question()
    with allure.step('Отображается сообщение об ошибке дубликата'):
        assert questions_page.get_duplicate_error_message() == 'Testing test test', \
        "Не найдена запись о наличии дубликата 'Testing test test'"

@pytest.mark.skip
def test_discard_question(questions_page, authenticated_user):
    questions_page.page.goto('https://stackoverflow.com/questions/ask')
    questions_page.page.on("dialog", lambda dialog: dialog.accept())
    questions_page.discard_button.click()
    #assert

@pytest.mark.xfail
def test_create_question(questions_page, authenticated_user):
    with allure.step('Перейти на страницу Questions нажатием кнопки'):
        questions_page.go_to_questions_page()
    with allure.step('Принять cookies'):
        questions_page.accept_cookies()
    with allure.step('Начать создание вопроса'):
        questions_page.start_question_creation()
    with allure.step('Заполнить заголовок вопроса'):
        questions_page.fill_question_title("Testing test test")
    with allure.step('Заполнить детали проблемы, описание ожидаемого результата'):
        questions_page.fill_problem_details("Lorem ipsum dolor sit amet...",
                                            "Sed ut perspiciatis unde omnis...")
    with allure.step('Заполнить теги'):
        questions_page.fill_tags("testing")
    with allure.step('Отметить, что вопрос не является дубликатом'):
        questions_page.mark_as_not_duplicate()
    with allure.step('Перейти к просмотру вопроса'):
        questions_page.review_question()
    with allure.step('Опубликовать вопрос'):
        questions_page.post_question()
    #questions_page.page.pause()
    #assert