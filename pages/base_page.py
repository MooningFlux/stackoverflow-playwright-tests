from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None: #mb use locators file with all locators
        self.page = page
        #self.home_button = page.locator('.-link--channel-name.pl6', has_text='Home') #li.ps-relative:nth-child(1)
        self.home_button = page.get_by_role("link", name="Home", exact=True) #~for logged user
        self.questions_button = page.get_by_label("Primary").get_by_role("link", name="Questions", exact=True)
        self.tags_button = page.get_by_role("link", name="Tags", exact=True)
        self.saves_button = page.get_by_role("link", name="Saves", exact=True) #for logged user
        self.users_button = page.get_by_role("link", name="Users", exact=True)
        self.companies_button = page.locator('#nav-companies') #page.get_by_role("link", name="Companies", exact=True)
        self.discussions_button = page.get_by_role("link", name="Discussions Labs", exact=True) #page.locator('#nav-labs-discussions')
        self.collectives_button = page.get_by_role("link", name="Explore all Collectives", exact=True)
        self.user_profile_button = page.locator('#user-profile-button')
        self.site_switcher = page.get_by_role("menuitem", name="Site switcher", exact=True) #page.locator('[aria-label="Site switcher"]')
        self.logout_link = page.get_by_role("link", name="log out")
        self.logout_button = page.get_by_role("button", name="Log out")
        self.login_dashboard_button = page.get_by_role("menuitem", name="Log in")
        self.search_input = page.locator('#search [name="q"]')
        self.search_caption_result = page.get_by_text("Results for").nth(0) #/search result


    def go_to_home_page(self) -> None:
        """Переход на страницу Home нажатием кнопки https://stackoverflow.com/""" 
        self.home_button.click()

    def go_to_saves_page(self) -> None:
        """Переход на страницу Saves нажатием кнопки https://stackoverflow.com/users/saves/21075508/all""" #user id extr
        self.saves_button.click()

    def go_to_questions_page(self) -> None:
        """Переход на страницу Questions нажатием кнопки https://stackoverflow.com/questions"""
        self.questions_button.click()
    
    def go_to_tags_page(self) -> None:
        """Переход на страницу Tags нажатием кнопки https://stackoverflow.com/tags"""
        self.tags_button.click()

    def go_to_users_page(self) -> None:
        """Переход на страницу Users нажатием кнопки https://stackoverflow.com/users"""
        self.users_button.click()

    def go_to_companies_page(self) -> None:
        """Переход на страницу Companies нажатием кнопки https://stackoverflow.com/jobs/companies"""
        self.companies_button.click()

    def go_to_discussions_page(self) -> None:
        """Переход на страницу Discussions нажатием кнопки https://stackoverflow.com/beta/discussions"""
        self.discussions_button.click()
    
    def go_to_collectives_page(self) -> None:
        """Переход на страницу Collectives нажатием кнопки https://stackoverflow.com/collectives-all"""
        self.collectives_button.click()

    def navigate_base(self) -> None:
        """Переход на страницу stackoverflow/questions"""
        self.page.goto('https://stackoverflow.com/questions', wait_until='commit')
        
    def navigate_login(self) -> None:
        """Открывает страницу логина.""" 
        self.page.goto('https://stackoverflow.com/users/login')
    
    def navigate_tags(self) -> None:
        """Открывает страницу тегов.""" 
        self.page.goto('https://stackoverflow.com/tags')
    
    def navigate(self, url: str) -> None:
        """Переход на указанный url"""
        self.page.goto(url, wait_until= 'domcontentloaded')
    
    #delete
    def title(self) -> str:
        """Возвращает заголовок страницы, same as page.title()"""
        return self.page.title() #delegated .title() call
    
    def logout(self) -> None:
        """Выполнить выход из профиля"""
        self.site_switcher.click()
        self.logout_link.click()
        self.logout_button.click()
    
    def search(self, phrase: str) -> None:
        """Выполнить поиск указанной phrase"""
        self.search_input.fill(phrase)
        self.search_input.press("Enter")
    
    def get_search_results_caption(self) -> str:
        """Возвращает значение надписи поискового запроса"""
        return self.search_caption_result.inner_text()