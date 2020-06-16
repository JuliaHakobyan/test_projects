import unittest
from selenium import webdriver
from new_project.herokuapp.pages.login_page import LoginPage
from new_project.herokuapp.pages.secure_page import SecurePage
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_logout(self):
        login_page = LoginPage(self.driver)
        secure_page = SecurePage(self.driver)
        login_page.with_("tomsmith", "SuperSecretPassword!")
        assert secure_page.login_success_message_present()
        secure_page.logout()
        assert login_page.logout_success_message_present()
        time.sleep(2)
        print(self.driver.current_url)




