import pytest
import allure
import requests
from playwright.sync_api import expect

base_url = "https://api.stackexchange.com/2.3/tags"

@allure.feature('Пагинация тегов')
class TestTagsPagination:
    @allure.story('UI тесты пагинации')
    @allure.title('Проверка количества тегов на странице по умолчанию (36)')
    def test_default_tags_per_page(self, tags_page):
        """Проверка что на странице отображается 36 тегов по умолчанию"""
        with allure.step('Открыть страницу тегов'):
            tags_page.navigate_tags()
        with allure.step('Проверить количество тегов на странице'):
            assert tags_page.get_tags_count() == 36, "Количество тегов на странице должно быть 36"

    @allure.story('UI тесты пагинации')
    @allure.title('Проверка перехода между страницами')
    @pytest.mark.parametrize('page_number', [1, 2, 3]) #1,2,3
    def test_pagination_navigation(self, tags_page, page_number):
        """Проверка корректности перехода между страницами"""
        with allure.step(f'Перейти на страницу {page_number}'):
            tags_page.navigate_to_page(page_number)
        with allure.step('Проверить номер текущей страницы'):
            assert tags_page.get_current_page_number() == page_number
        with allure.step('Проверить количество тегов на странице'):
            assert tags_page.get_tags_count() == 36

    @allure.story('API тесты пагинации')
    @allure.title('Проверка размера страницы через API')
    @pytest.mark.api
    @pytest.mark.parametrize('page_size', [15, 30, 36])
    def test_api_pagination_pagesize(self, page_size):
        """Проверка корректности количества тегов при разных значениях pagesize"""
        with allure.step(f'Отправить API запрос с pagesize={page_size}'):
            response = requests.get(
                base_url,
                params={
                    "page": 1,
                    "pagesize": page_size,
                    "order": "desc",
                    "sort": "popular",
                    "site": "stackoverflow",
                    "key": "rl_bDjukFK2wQnvjqrqBVhCHDEWp"
                }
            )
        
        with allure.step('Проверить статус ответа'):
            assert response.status_code == 200
            
        with allure.step('Проверить количество полученных тегов'):
            assert len(response.json()['items']) == page_size

    @allure.story('Комбинированные тесты UI+API')
    @allure.title('Сравнение данных пагинации между UI и API')
    @pytest.mark.uiapi
    def test_ui_api_pagination_consistency(self, tags_page):
        """Проверка соответствия данных пагинации между UI и API"""
        with allure.step('Открыть страницу тегов в UI'):
            tags_page.navigate_tags()
            ui_tags_count = tags_page.get_tags_count()
            
        with allure.step('Получить данные через API'):
            response = requests.get(
                base_url,
                params={
                    "page": 1,
                    "pagesize": 36,
                    "order": "desc",
                    "sort": "popular",
                    "site": "stackoverflow",
                    "key": "rl_bDjukFK2wQnvjqrqBVhCHDEWp"
                }
            )
            api_tags_count = len(response.json()['items'])
            
        with allure.step('Сравнить количество тегов в UI и API'):
            assert ui_tags_count == api_tags_count, \
                "Количество тегов в UI и API должно совпадать"
    
    #delete        
    @pytest.mark.api
    def test_pagination_pagesize(self): #pagesize=36, requests used
        r = requests.get("https://api.stackexchange.com/2.3/tags?page=1&pagesize=36&order=desc&sort=popular&site=stackoverflow")
        data = r.json()
        assert r.status_code == 200 #
        assert len(data['items']) == 36

    @pytest.mark.api
    def test_pagination_empty_page(self, tags_page): #page.request used
        r = tags_page.page.request.get(
            base_url,
            params={
                "page": 999999,
                "pagesize": 36,
                "order": "desc",
                "sort": "popular",
                "site": "stackoverflow",
                "key": "rl_bDjukFK2wQnvjqrqBVhCHDEWp"
            }
        )
        data = r.json()
        print(data)
        assert r.status == 200
        assert len(data["items"]) == 0  # Пустая страница

    @allure.story('UI тесты пагинации')
    @allure.title('Проверка отображения кнопки Prev на 1 странице')
    def test_pagination_prev_button_on_first_page(self, tags_page):
        """Проверка что на 1 странице не отображается кнопка Prev"""
        with allure.step('Открыть страницу тегов'):
            tags_page.navigate_to_page(1)
        with allure.step('Проверить номер текущей страницы'):
            assert tags_page.get_current_page_number() == 1
        with allure.step('Проверить отображение кнопки Prev'):
            assert tags_page.is_prev_button_present() == False, "Кнопка Prev не должна отображаться на 1 странице"


@allure.title('MOCK: Проверка размера страницы через API')
@pytest.mark.api
def test_api_pagination_pagesize_mock(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': [1, 1, 1]}  #3 tags

    # Мокаем requests.get, чтобы он возвращал наш мок-ответ
    mock_get = mocker.patch('requests.get', return_value=mock_response)

    # Теперь вызов requests.get вернёт mock_response
    with allure.step(f'Отправить API запрос с pagesize = 3'):
        response = requests.get(
            base_url,
            params={
                        "page": 1,
                        "pagesize": 3,
                        "order": "desc",
                        "sort": "popular",
                        "site": "stackoverflow",
                        "key": "rl_bDjukFK2wQnvjqrqBVhCHDEWp"
                    })
    with allure.step('Проверить статус ответа'):
        assert response.status_code == 200
    with allure.step('Проверить количество тегов на странице'):
        assert len(response.json()['items']) == 3
    mock_get.assert_called_once_with(base_url,
            params={
                        "page": 1,
                        "pagesize": 3,
                        "order": "desc",
                        "sort": "popular",
                        "site": "stackoverflow",
                        "key": "rl_bDjukFK2wQnvjqrqBVhCHDEWp"
                    })