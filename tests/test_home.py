import pytest
import allure
from playwright.sync_api import expect

#class name?
def test_welcome_message(home_page, authenticated_user):
    with allure.step('Перейти на на страницу Home нажатием кнопки'):
        home_page.go_to_home_page()
    with allure.step('Отображается приветственное сообщение с именем пользователя: Welcome to Stack Overflow, <username>'):
        profile_name = home_page.get_user_profile_name()
        assert home_page.get_welcome_message() == f'Welcome to Stack Overflow, {profile_name}!' or f'Welcome back, {profile_name}'