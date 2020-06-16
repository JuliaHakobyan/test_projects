from selenium.webdriver.common.by import By
from new_project.herokuapp.pages.login_page import LoginPage

class SecurePage(LoginPage):
    secure_area_title = {"by": By.CLASS_NAME, "value": "icon-lock"}
    welcome_text = {"by": By.CLASS_NAME, "value": "subheader"}
    logout_button = {"by": By.XPATH, "value": "//a[@class='button secondary radius']"}
    login_success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    login_success_message_close = {"by": By.XPATH, "value": "//a[@class='close']"}

    def __init__(self, driver):
        super().__init__(driver)
        self.visit("http://the-internet.herokuapp.com/login")
        assert self.is_displayed(self.login_form)

    def logout(self):
        self.click(self.logout_button)

    def login_success_message_present(self):
        return self.is_displayed(self.login_success_message)

    def close_login_message(self):
        self.click(self.login_success_message_close)
