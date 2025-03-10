from playwright.sync_api import Page
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class BasePage:
    def __init__(self, page: Page): #mb use locators file with all locators
        self.page = page
        #self.home_button = page.locator('.-link--channel-name.pl6', has_text='Home') #li.ps-relative:nth-child(1)
        self.home_button = page.get_by_role("link", name="Home", exact=True) #kinda for logged user
        self.questions_button = page.get_by_label("Primary").get_by_role("link", name="Questions", exact=True)
        self.tags_button = page.get_by_role("link", name="Tags", exact=True)
        self.saves_button = page.get_by_role("link", name="Saves", exact=True) #for logged user
        self.users_button = page.get_by_role("link", name="Users", exact=True)
        self.companies_button = page.get_by_role("link", name="Companies", exact=True)
        self.discussions_button = page.get_by_role("link", name="Discussions", exact=True)
        self.collectives_button = page.get_by_role("link", name="Explore all Collectives", exact=True)

        self.user_profile_button = page.locator('#user-profile-button')

    def go_to_home_page(self):
        """Переход на страницу Home нажатием кнопки https://stackoverflow.com/""" 
        self.home_button.click()

    def go_to_saves_page(self):
        """Переход на страницу Saves нажатием кнопки https://stackoverflow.com/users/saves/21075508/all""" #user id extr
        self.saves_button.click()

    def go_to_questions_page(self):
        """Переход на страницу Questions нажатием кнопки https://stackoverflow.com/questions"""
        self.questions_button.click()
    
    def go_to_tags_page(self):
        """Переход на страницу Tags нажатием кнопки https://stackoverflow.com/tags"""
        self.tags_button.click()

    def go_to_users_page(self):
        """Переход на страницу Users нажатием кнопки https://stackoverflow.com/users"""
        self.users_button.click()

    def go_to_companies_page(self):
        """Переход на страницу Companies нажатием кнопки https://stackoverflow.com/jobs/companies"""
        self.companies_button.click()

    def go_to_discussions_page(self):
        """Переход на страницу Discussions нажатием кнопки https://stackoverflow.com/beta/discussions"""
        self.discussions_button.click()
    
    def go_to_collectives_page(self):
        """Переход на страницу Collectives нажатием кнопки https://stackoverflow.com/collectives-all"""
        self.collectives_button.click()

    def navigate_base(self):
        """Переход на страницу stackoverflow/questions"""
        self.page.goto('https://stackoverflow.com/questions', wait_until='commit') #tweak option, use best practice