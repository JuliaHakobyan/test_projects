from selenium.webdriver.common.by import By
from herokuapp.pages.login_page import LoginPage

class AuthorizationPage(LoginPage):
    secure_area_title = {"by": By.CLASS_NAME, "value": "icon-lock"}
    welcome_text = {"by": By.CLASS_NAME, "value": "subheader"}
    logout_button = {"by": By.CLASS_NAME, "value": "icon-2x icon-signout"}
    logout_message = {"by": By.ID, "value": "flash"}

    def __init__(self, driver):
        assert self.is_displayed(self.login_form)

    def logout(self):
        self.click(self.logout_button)

    def logout_success_message_present(self):
        return self.is_displayed(self.logout_success_message_present())
