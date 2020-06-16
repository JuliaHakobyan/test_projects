import unittest
from selenium import webdriver
from new_project.herokuapp.pages.home_page import HomePage
from new_project.herokuapp.pages.login_page import LoginPage


class HomeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()

    def select_loginpage(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)

        home_page.select_login_page()
        #assert login_page.login_form_present()
        #assert login_page.is_displayed(login_page.login_form_present())
        assert login_page.login_form_present()
