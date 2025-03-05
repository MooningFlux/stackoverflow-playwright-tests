import pytest
#from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login_failure(login_page):
    #login_page = LoginPage(page)
    login_page.navigate()
    login_page.login('nikolai.sazonov.99@gmail.com', '12312asd')
    assert login_page.get_error_message() == 'The email or password is incorrect.', \
        "Не найдена запись о 'The email or password is incorrect.'"
    
def test_click_tags_button(login_page):
    #login_page = LoginPage(page)
    login_page.navigate_base()
    login_page.go_to_tags_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    assert login_page.title() == 'Tags - Stack Overflow'

@pytest.mark.parametrize('email, password', [
    ('nikolai.sazonov.99@gmail.com', 'correctpass'),
    ('admin', 'admin') #incorrect creds
])
def test_login_success(login_page, email, password):
    #login_page = LoginPage(page)
    login_page.navigate() #rename to navigate to login page
    login_page.login(email, password)
    #expect(page).to_have_url("https://stackoverflow.com/")
    expect(login_page.user_profile_button).to_be_visible()

    #TODO: correct password containment, 