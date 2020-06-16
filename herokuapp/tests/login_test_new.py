import unittest
from selenium import webdriver
from new_project.herokuapp.pages.login_page import LoginPage
from new_project.herokuapp.pages.secure_page import SecurePage
from new_project.herokuapp.pages.base_page import BasePage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_login_logout(self):
        login_page = LoginPage(self.driver)
        secure_page = SecurePage(self.driver)

        login_page.with_("tomsmith", "SuperSecretPassword!")
        assert secure_page.login_success_message_present()
        secure_page.logout()
        assert login_page.logout_success_message_present()