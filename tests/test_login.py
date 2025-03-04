from pages.login_page import LoginPage

from playwright.sync_api import expect


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('nikolai.sazonov.99@gmail.com', '12312asd')
    assert login_page.get_error_message() == 'The email or password is incorrect.', \
        "Не найдена запись о 'The email or password is incorrect.'"
    
def test_click_tags_button(page):
    login_page = LoginPage(page)
    login_page.navigate_base()
    login_page.go_to_tags_page()
    assert page.title() == 'Tags - Stack Overflow'

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.navigate() #rename to navigate to login page
    login_page.login('correct_email', 'correct_password')
    expect(login_page.user_profile_button).to_be_visible()