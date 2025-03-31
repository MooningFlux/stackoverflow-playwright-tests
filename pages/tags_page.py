from playwright.sync_api import Page
from pages.base_page import BasePage

class TagsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.pagination_buttons = page.locator('.s-pagination--item') #filter
        self.current_page_button = page.locator('.s-pagination--item.is-selected')
        self.tags_list = page.locator('#tags-browser .s-card') # tags containers
        self.next_page_button = page.get_by_role("link", name="Next", exact=True)
        self.prev_page_button = page.get_by_role("link", name="Prev", exact=True)

    def navigate_to_page(self, page_number: int) -> None:
        """Перейти на указанную страницу"""
        if not isinstance(page_number, int) or page_number < 1:
            raise ValueError("Номер страницы должен быть положительным целым числом")
        self.page.goto(f'https://stackoverflow.com/tags?page={page_number}&tab=popular')
        
    def get_tags_count(self) -> int:
        """Возвращает количество тегов на странице"""
        return self.tags_list.count()
        
    def get_current_page_number(self) -> int:
        """Возвращает номер текущей страницы"""
        return int(self.current_page_button.inner_text())
                   #.filter(has=self.page.locator('.is-selected')).inner_text()))

    def is_prev_button_present(self) -> bool:
        """Возвращает признак отображения кнопки Prev"""
        return self.prev_page_button.is_visible()