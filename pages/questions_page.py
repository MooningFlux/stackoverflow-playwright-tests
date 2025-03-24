from playwright.sync_api import Page
from pages.base_page import BasePage
from datetime import datetime


class QuestionsPage(BasePage):
    def __init__(self, page: Page): #mb use locators file with all locators
        super().__init__(page)
        self.ask_question_button = page.get_by_role("link", name="Ask Question")
        #ask page
        self.question_title_input = page.locator('#title')
        self.next_button = page.get_by_role("button", name="Next")
        self.problem_details_input = page.locator("#problem-details").get_by_role("textbox", name="Body")
        self.problem_results_input = page.locator("#problem-results").get_by_role("textbox", name="Body")
        self.tags_input = page.locator('#tageditor-replacing-tagnames--input') #page.get_by_role("combobox", name="Tags Add up to 5 tags to")
        self.tags_editor = page.locator('.js-tag-editor') #mb change - for accepting tag in tag pad
        self.review_button = page.get_by_role("button", name="Review your question") #locator('button.js-review-question-button') # button.js-begin-review-button | page.get_by_role("button", name="Review your question")
        self.discard_button = page.get_by_role("button", name="Discard draft") #page.locator('button.js-discard-question')
        self.discard_cancel_button = page.locator('#discard-cancel-btn') #page.get_by_role("button", name="Continue editing")
        self.discard_confirmation_button = page.locator('#discard-confirmation-btn') #page.get_by_role("button", name="Discard question")
        self.post_question_button = page.get_by_role("button", name="Post your question") #page.locator('#submit-button')
        self.cookies_button = page.get_by_role("button", name="Accept all cookies")
        self.not_duplicate_checkbox = page.locator('#verify-not-duplicate')
        self.duplicate_message = page.locator('.question-hyperlink')
        #modified for TestAccount
        self.body_input = page.locator('#wmd-input') # body input for test account
        
    def accept_cookies(self):
        """Принять cookies"""
        self.cookies_button.click()

    def start_question_creation(self):
        """Нажать на кнопку создания вопроса"""
        self.ask_question_button.click()
    
    def fill_question_title(self, title: str):
        """Заполнить заголовок вопроса"""
        self.question_title_input.fill(title)
        self.next_button.click()
    
    def fill_problem_details(self, details: str, results: str):
        """Заполнить детали вопроса и ожидаемый результат"""
        self.problem_details_input.fill(details)
        #self.problem_details_input.fill("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        self.problem_details_input.type(" ")
        self.problem_details_input.press("Backspace")
        self.next_button.click()
        self.problem_results_input.fill(results)
        #self.problem_results_input.fill("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.")
        self.problem_results_input.type(" ") #add date to differentiate texts
        self.problem_results_input.press("Backspace")
        self.next_button.click()
    
    def fill_tags(self, tags: str):
        """Заполнить теги"""
        self.tags_input.fill("testing")
        self.tags_editor.click() #position={ "x": 90, "y": 0}
        self.next_button.click()

    def mark_as_not_duplicate(self):
        """Отметить, что вопрос не дубликат"""
        self.not_duplicate_checkbox.check()

    def review_question(self):
        """Перейти к ревью вопроса"""
        self.review_button.click()
    
    def post_question(self):
        """Опубликовать вопрос"""
        self.post_question_button.click()

    def ask_correct_question(self): #decompose on smaller actions, include them in this action
        """Создание вопроса"""
        self.accept_cookies()
        self.start_question_creation()
        self.fill_question_title("Testing test test")
        self.fill_problem_details("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                                  "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.")
        self.fill_tags("testing")
        self.mark_as_not_duplicate()
        self.review_question()
        self.post_question()
        # self.cookies_button.click()
        # self.ask_question_button.click()
        # self.question_title_input.fill("Testing test test")
        # self.next_button.click()
        # self.problem_details_input.fill("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        # self.problem_details_input.type(" ")
        # self.problem_details_input.press("Backspace")
        # self.next_button.click()
        # self.problem_results_input.fill("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.")
        # self.problem_results_input.type(" ") #add date to differentiate texts
        # self.problem_results_input.press("Backspace")
        # self.next_button.click()
        # self.tags_input.fill("testing")
        # self.tags_editor.click() #change on different locator| position={ "x": 90, "y": 0}
        # #self.page.pause()
        # self.next_button.click()
        # self.not_duplicate_checkbox.check()
        # self.review_button.click()
        # self.post_question_button.click()
        #captcha

    def ask_correct_modified_question(self): #for TestAccount
        """Создание вопроса (TestAccount)"""
        self.cookies_button.click() #check
        self.ask_question_button.click()
        self.question_title_input.fill("Testing test test")
        self.body_input.fill("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. ")
        self.tags_input.fill("testing")
        self.tags_editor.click()
        self.review_button.click()
        self.post_question_button.click()

    def discard_questions(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.discard_button.click()

    def get_duplicate_error_message(self):
        """Возвращает название поста дубликата"""
        return self.duplicate_message.inner_text()