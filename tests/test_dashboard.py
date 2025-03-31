import pytest
import allure
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

# @pytest.mark.parametrize("search_phrase", [
#     "Cannot read properties of undefined",
#     "But it works on my machine"
# ])
def test_search(base_page):
    SEARCH_PHRASE = "Cannot read properties of undefined"
    base_page.navigate_base()
    base_page.search(SEARCH_PHRASE) #parametrize, use const
    #expect for search phrase to be present in search bar
    assert SEARCH_PHRASE.lower() in base_page.get_search_results_caption().lower(), \
    f"{SEARCH_PHRASE}: должен содержаться в надписи результата поиска"
    base_page.page.pause()