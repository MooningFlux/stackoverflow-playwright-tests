from playwright.sync_api import Page
from pages.base_page import BasePage


class QuestionsPage(BasePage):
    def __init__(self, page: Page): #mb use locators file with all locators
        #BasePage.__init__(self, page)
        super().__init__(page)
        self.ask_question_button = page.get_by_role("link", name="Ask Question")
        #ask page
        self.question_title_input = page.locator('#title')
        self.next_button = page.get_by_role("button", name="Next")
        self.problem_details_input = page.locator("#problem-details").get_by_role("textbox", name="Body")
        self.problem_results_input = page.locator("#problem-results").get_by_role("textbox", name="Body")
        self.tags_input = page.locator('#tageditor-replacing-tagnames--input') #page.get_by_role("combobox", name="Tags Add up to 5 tags to")
        self.tags_editor = page.locator('.js-tag-editor') #mb change - for accepting tag in tag pad
        self.review_button = page.locator('button.js-review-question-button') #page.get_by_role("button", name="Review your question")
        self.discard_button = page.locator('button.js-discard-question') #page.get_by_role("button", name="Discard draft")
        self.discard_cancel_button = page.locator('#discard-cancel-btn') #page.get_by_role("button", name="Continue editing")
        self.discard_confirmation_button = page.locator('#discard-confirmation-btn') #page.get_by_role("button", name="Discard question")
        self.post_question_button = page.get_by_role("button", name="Post your question") #page.locator('#submit-button')
        self.cookies_button = page.get_by_role("button", name="Accept all cookies")
        self.not_duplicate_checkbox = page.locator('#verify-not-duplicate')

    def ask_correct_question(self): #decompose on smaller actions, include them in this test
        """Создание вопроса"""
        self.cookies_button.click() #check
        self.ask_question_button.click()
        self.question_title_input.fill("Testing test test")
        self.next_button.click()
        self.problem_details_input.fill("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        self.problem_details_input.type(" ")
        self.next_button.click()
        self.problem_results_input.fill("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.")
        self.problem_results_input.type(" ")
        self.next_button.click()
        self.tags_input.fill("testing")
        self.tags_editor.click() #change on different locator| position={ "x": 90, "y": 0}
        #self.page.pause()
        self.next_button.click()
        self.not_duplicate_checkbox.check()
        self.review_button.click()
        #expect Please do a final review of your question and then post.
        self.post_question_button.click()
        #captcha?