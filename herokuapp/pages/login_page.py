from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from new_project.herokuapp.pages.base_page import BasePage


class LoginPage(BasePage):
    login_page_title = {"by": By.CLASS_NAME, "value": "Login Page"}
    login_form = {"by": By.ID, "value": "login"}
    username_input = {"by": By.ID, "value": "username"}
    password_input = {"by": By.ID, "value": "password"}
    submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    login_failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    logout_success_message = {"by": By.CSS_SELECTOR, "value": "#flash-messages"}
    logout_success_message_close = {"by": By.XPATH, "value": "//a[@class='close']"}

    #def __init__(self, driver):
        #super().__init__(driver)
        #self.visit("http://the-internet.herokuapp.com/login")
        #assert self.is_displayed(self.login_form)

    def login_form_present(self):
        return self.is_displayed(self.login_form)

    def with_(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.submit_button)

    def login_failure_message_present(self):
        return self.is_displayed(self.login_failure_message)

    def logout_success_message_present(self):
        return self.is_displayed(self.logout_success_message)

    def close_logout_message(self):
        self.click(self.logout_success_message_close)

    def visit_homepage(self, url):
        self.driver.maximize_window()
        self.driver.get("http://the-internet.herokuapp.com/")

