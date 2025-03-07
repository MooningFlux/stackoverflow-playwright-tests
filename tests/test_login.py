import pytest
import allure
#from pages.login_page import LoginPage
from decouple import config
from playwright.sync_api import expect

EMAIL = config('EMAIL') #temporary till CI secrets
#PASSWORD = config('PASSWORD')
NOTPASSWORD = config('NOTPASSWORD')

@allure.feature('Вход в систему (Login)')
@allure.story('Авторизация с неверными данными')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Тест входа с неправильными учетными данными...")
@allure.title('Авторизация с некорректными учетными данными')
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate_login()
    with allure.step('Ввести в форму авторизации некорректные учетные данные'):
        login_page.login(EMAIL, '12312asd')
    with allure.step('Отображается сообщение об ошибке'):
        assert login_page.get_error_message() == 'The email or password is incorrect.', \
        "Не найдена запись о 'The email or password is incorrect.'"
    
@allure.feature('Навигационная панель')
@allure.story('Переход на страницу /tags')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Переход со страницы /questions на страницу /tags нажатием соответствующей кнопки")
@allure.title('Переход со страницы /questions на страницу /tags')
def test_click_tags_button(login_page):
    with allure.step('Открыть страницу stackoverflow/questions'):
        login_page.navigate_base()
    with allure.step('Перейти на на страницу Tags нажатием кнопки'):
        login_page.go_to_tags_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    with allure.step('Отображается название страницы: Tags - Stack Overflow'):
        assert login_page.title() == 'Tags - Stack Overflow'

@allure.feature('Вход в систему (Login)')
@allure.story('Успешная авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с корректными учетными данными')
@pytest.mark.parametrize('email, password', [
    (EMAIL, NOTPASSWORD),
    ('admin', 'admin') #future correct creds (create test account)
])
def test_login_success(login_page, email, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate_login()
    with allure.step('Ввести в форму авторизации корректные учетные данные'):
        login_page.login(email, password)
    #expect(login_page.page).to_have_url("https://stackoverflow.com/")
    with allure.step('Отображается профиль пользователя в дешборде'):
        expect(login_page.user_profile_button).to_be_visible()

#TODO: ci implementation, write and automate test cases (add API tests)