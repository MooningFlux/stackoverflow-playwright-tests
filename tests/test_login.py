import pytest
import allure
#from pages.login_page import LoginPage
from decouple import config
from tests.conftest import EMAIL, PASSWORD, EMAIL2, PASSWORD2
from playwright.sync_api import expect


@allure.feature('Вход в систему (Login)')
@allure.story('Авторизация с неверными данными')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('Тест входа с неправильными учетными данными')
@allure.title('Авторизация с некорректными учетными данными')
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate('https://stackoverflow.com/users/login')
    with allure.step('Ввести в форму авторизации некорректные учетные данные'):
        login_page.login(EMAIL, '12312asd')
    with allure.step('Отображается сообщение об ошибке'):
        assert login_page.get_error_message() == 'The email or password is incorrect.', \
        "Не найдена запись о 'The email or password is incorrect.'"


#move to test_dashboard.py
@pytest.mark.need_review
@allure.feature('Навигационная панель')
@allure.story('Переход на страницу /tags')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Переход со страницы /questions на страницу /tags нажатием соответствующей кнопки")
@allure.title('Переход со страницы /questions на страницу /tags')
#@pytest.mark.only_browser('firefox')
def test_click_tags_button(login_page, browser_name):
    with allure.step(f'Запустить тест в браузере {browser_name}'):
        with allure.step('Открыть страницу stackoverflow/questions'):
            login_page.navigate_base()
        with allure.step('Перейти на на страницу Tags нажатием кнопки'):
            login_page.go_to_tags_page()
        with allure.step('Отображается название страницы: Tags - Stack Overflow'):
            assert login_page.title() == 'Tags - Stack Overflow'
#Объединить тесты в класс? Чтобы не было перегружено @allure

def test_click_users_button(login_page): #login_page -> questions_page ?
    with allure.step('Открыть страницу stackoverflow/questions'):
        login_page.navigate_base()
    with allure.step('Перейти на на страницу Users нажатием кнопки'):
        login_page.go_to_users_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    with allure.step('Отображается название страницы: Users - Stack Overflow'):
        assert login_page.title() == 'Users - Stack Overflow'

def test_click_companies_button(login_page):
    with allure.step('Открыть страницу stackoverflow/questions'):
        login_page.navigate_base()
    with allure.step('Перейти на на страницу Companies нажатием кнопки'):
        login_page.go_to_companies_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    with allure.step('Отображается название страницы: Best Companies Hiring Developers - Stack Overflow'):
        assert login_page.title() == 'Best Companies Hiring Developers - Stack Overflow'

def test_click_discussions_button(login_page):
    with allure.step('Открыть страницу stackoverflow/questions'):
        login_page.navigate_base()
    with allure.step('Перейти на на страницу Discussions нажатием кнопки'):
        login_page.go_to_discussions_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    with allure.step('Отображается название страницы: Discussions - Stack Overflow'):
        assert login_page.title() == 'Discussions - Stack Overflow'

def test_click_collectives_button(login_page):
    with allure.step('Открыть страницу stackoverflow/questions'):
        login_page.navigate_base()
    with allure.step('Перейти на на страницу Collectives нажатием кнопки'):
        login_page.go_to_collectives_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    with allure.step('Отображается название страницы: Explore all Collectives™ on Stack Overflow'):
        assert login_page.title() == 'Explore all Collectives™ on Stack Overflow'

def test_click_questions_button(login_page):
    #add login here...
    with allure.step('Открыть страницу stackoverflow/tags'):
        login_page.navigate_tags()
    with allure.step('Перейти на страницу Questions нажатием кнопки'):
        login_page.go_to_questions_page()
    with allure.step('Отображается название страницы: Newest Questions - Stack Overflow'):
        assert login_page.title() == 'Newest Questions - Stack Overflow'
##########################################################

@allure.feature('Вход в систему (Login)')
@allure.story('Успешная авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('email, password', [
    pytest.param(EMAIL, PASSWORD, marks=pytest.mark.xfail),
    (EMAIL2, PASSWORD2) #Secret used in remote repo
])
def test_login_success(login_page, email, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate_login()
    with allure.step('Ввести в форму авторизации корректные учетные данные'):
        login_page.login(email, password)
    #expect(login_page.page).to_have_url("https://stackoverflow.com/")
    with allure.step('Отображается профиль пользователя в дешборде'):
        expect(login_page.user_profile_button).to_be_visible()

#################### Tests for logged in user -> tests_questions
    

#TODO: write and automate test cases: add main functions tests, add API tests; use xdist, add different environments?
#https://api.stackexchange.com/docs - API
#DONE:

#EMAIL2, PASSWORD2 - test account
#KISS, Arrange – Act – Assert
