import unittest
from selenium import webdriver
from new_project.herokuapp.pages.home_page import HomePage
from new_project.herokuapp.pages.login_page import LoginPage
import time


class HomeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.quit()

    def test_select_loginpage(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.select_login_page()
        assert login_page.login_form_present()
        time.sleep(2)


