from selenium.webdriver.common.by import By

from new_project.herokuapp.pages import login_page
from new_project.herokuapp.pages.base_page import BasePage


class HomePage(BasePage):
    home_page_title = {"by": By.CLASS_NAME, "value": "heading"}
    home_page_departments_list = {"by": By.XPATH, "value": "//*[@id='content']/h2"}
    login_page_selection = {"by": By.CSS_SELECTOR, "value": "//*[@id='content']/ul/li[21]/a"}

    def __init__(self, driver):
        super().__init__(driver)
        self.visit("http://the-internet.herokuapp.com/")
        assert self.is_displayed(self.home_page_title)

    def select_login_page(self):
        self.click(self.login_page_selection)
