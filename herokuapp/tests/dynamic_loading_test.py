import unittest
from selenium import webdriver
from new_project.herokuapp.pages import dynamic_loading_page
from new_project.herokuapp.pages.dynamic_loading_page import DynamicLoadingPage
from new_project.herokuapp.pages.home_page import HomePage
import time


class DinamicTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_dynamic_page_present(self):
        home_page = HomePage(self.driver)
        dynamic_loading_page = DynamicLoadingPage(self.driver)
        home_page.select_dynamic_loading()
        assert dynamic_loading_page.dynamic_page_title_present()

        dynamic_loading_page.click_example_1()
        assert dynamic_loading_page.example_1_start_present
        dynamic_loading_page.example_1_start_button_present()
        assert dynamic_loading_page.example_1_start_present
        time.sleep(3)



