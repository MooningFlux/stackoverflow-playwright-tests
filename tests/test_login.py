import pytest
#from pages.login_page import LoginPage
from decouple import config
from playwright.sync_api import expect

EMAIL = config('EMAIL') #temporary till CI secrets
PASSWORD = config('PASSWORD')

def test_login_failure(login_page):
    #login_page = LoginPage(page)
    #email = config('EMAIL')
    #password = config('PASSWORD')

    login_page.navigate()
    login_page.login(EMAIL, '12312asd')
    assert login_page.get_error_message() == 'The email or password is incorrect.', \
        "Не найдена запись о 'The email or password is incorrect.'"
    
def test_click_tags_button(login_page):
    login_page.navigate_base()
    login_page.go_to_tags_page()
    #assert login_page.page.title() == 'Tags - Stack Overflow' #encapsulation violation
    assert login_page.title() == 'Tags - Stack Overflow'

@pytest.mark.parametrize('email, password', [
    (EMAIL, PASSWORD),
    ('admin', 'admin') #future correct creds (create test account)
])
def test_login_success(login_page, email, password):
    login_page.navigate_login()
    login_page.login(email, password)
    #expect(login_page.page).to_have_url("https://stackoverflow.com/")
    expect(login_page.user_profile_button).to_be_visible()

    #TODO: allure reporting, ci implementation