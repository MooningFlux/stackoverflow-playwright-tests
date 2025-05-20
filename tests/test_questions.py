import pytest
import allure
from playwright.sync_api import expect
from pages.questions_page import StackOverflowAPI

@pytest.mark.xfail #captcha
def test_create_duplicate_question(questions_page, authenticated_user): #in real projects - use api for authorization (auth cookies or mocks)
    with allure.step('Перейти на страницу Questions нажатием кнопки'): #by default after authorization user is redirected to /questions page
        questions_page.go_to_questions_page()
    #press ask question button
    with allure.step('Задать корректный вопрос'): #decompose
        questions_page.ask_correct_question()
        #questions_page.ask_correct_modified_question()
    with allure.step('Отображается сообщение об ошибке дубликата'):
        assert questions_page.get_duplicate_error_message() == 'Testing test test', \
        "Не найдена запись о наличии дубликата 'Testing test test'"
    #questions_page.discard_questions() #with slowmo 1500

@pytest.mark.skip
def test_discard_question(questions_page, authenticated_user): #xfail - must be empty/discarded
    questions_page.page.goto('https://stackoverflow.com/questions/ask')
    questions_page.page.on("dialog", lambda dialog: dialog.accept())
    questions_page.discard_button.click()
    #assert

@pytest.mark.xfail
def test_create_question(questions_page, authenticated_user): #xfail captcha
    with allure.step('Перейти на страницу Questions нажатием кнопки'):
        questions_page.go_to_questions_page()
    with allure.step('Принять cookies'):
        questions_page.accept_cookies()
    with allure.step('Начать создание вопроса'):
        questions_page.start_question_creation()
    with allure.step('Заполнить заголовок вопроса'):
        questions_page.fill_question_title("Testing test test")
        #expect(questions_page.question_title_input).to_have_value("Testing test test")
    with allure.step('Заполнить детали проблемы, описание ожидаемого результата'):
        questions_page.fill_problem_details("Lorem ipsum dolor sit amet...",
                                            "Sed ut perspiciatis unde omnis...") #220 chars
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

#delete
def test_API_users(page):
    response = page.request.get('https://api.stackexchange.com/2.3/users/29973352?site=stackoverflow')
    # print(response.status)
    # print(response.json())
    assert response.json()["items"][0]["display_name"] == "TestAccount"

@pytest.mark.xfail(reason="Expected xfail: cloudflare challenge")
@pytest.mark.parametrize("api_question_response", [4, 79535884], indirect=True)
def test_question_title_match(questions_page, api_question_response): #api combined with ui test
    api_title = StackOverflowAPI.extract_title_from_response(api_question_response)
    question_id = StackOverflowAPI.extract_id_from_response(api_question_response)
    
    questions_page.navigate_to_question_id(question_id)
    ui_title = questions_page.get_question_title()
    assert api_title == ui_title