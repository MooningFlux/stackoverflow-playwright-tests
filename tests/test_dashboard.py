import pytest
import allure
from decouple import config
from tests.conftest import EMAIL, PASSWORD, EMAIL2, PASSWORD2
from playwright.sync_api import expect


@allure.feature('Выход из профиля (Log out)')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Выход из профиля (Log Out), используя панель')
def test_logout(base_page, authenticated_user):
    with allure.step('Открыть главную страницу'):
        base_page.navigate('https://stackoverflow.com')
    with allure.step('Выйти из профиля'):
        base_page.logout()
    with allure.step('Отображается сообщение об ошибке'):
        expect(base_page.login_dashboard_button).to_be_visible()