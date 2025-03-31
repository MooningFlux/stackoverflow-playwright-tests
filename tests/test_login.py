import pytest
import allure
#from pages.login_page import LoginPage
from decouple import config
from tests.conftest import EMAIL, PASSWORD, EMAIL2, PASSWORD2
from playwright.sync_api import expect


@allure.feature('Вход в систему (Login)')
class TestLogin:
    @allure.story('Авторизация с неверными данными')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Тест входа с неправильными учетными данными')
    @allure.title('Авторизация с некорректными учетными данными')
    def test_login_failure(self, login_page):
        with allure.step('Открыть страницу авторизации'):
            login_page.navigate('https://stackoverflow.com/users/login')
        with allure.step('Ввести в форму авторизации некорректные учетные данные'):
            login_page.login(EMAIL, '12312asd')
        with allure.step('Отображается сообщение об ошибке'):
            assert login_page.get_error_message() == 'The email or password is incorrect.', \
            "Не найдена запись о 'The email or password is incorrect.'"

    @allure.story('Успешная авторизация')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Авторизация с корректными учетными данными')
    @pytest.mark.parametrize('email, password', [
        pytest.param(EMAIL, PASSWORD, marks=pytest.mark.xfail),
        (EMAIL2, PASSWORD2) #Secret used in remote repo
    ])
    def test_login_success(self, login_page, email, password):
        with allure.step('Открыть страницу авторизации'):
            login_page.navigate_login()
        with allure.step('Ввести в форму авторизации корректные учетные данные'):
            login_page.login(email, password)
        #expect(login_page.page).to_have_url("https://stackoverflow.com/")
        with allure.step('Отображается профиль пользователя в дешборде'):
            expect(login_page.user_profile_button).to_be_visible()

#TODO: add authentication fixture through api, write and automate test cases: add main functions tests; use xdist, 
#add different environments?

#EMAIL2, PASSWORD2 - test account
#KISS, Arrange – Act – Assert
