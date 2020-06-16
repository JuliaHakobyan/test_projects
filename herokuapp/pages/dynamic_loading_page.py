from selenium.webdriver.common.by import By
from herokuapp.pages.base_page import BasePage


class DynamicallyLoadedPage():
    dynamically_loaded_page_title = {"by": By.XPATH, "value": "//*[@id='content']/div/h3"}
    page_text_1 = {"by": By.XPATH, "value": "//*[@id='content']/div/p[1]/text()"}
    page_text_2 = {"by": By.XPATH, "value": "//*[@id='content']/div/p[2]/text()"}
    example_1 = {"by": By.XPATH, "value": "//*[@id='content']/div/a[1]"}
    example_2 = {"by": By.XPATH, "value": "//*[@id='content']/div/a[2]"}
    example_1_start_present = {"by": By.XPATH, "value": "//*[@id='start']/button"}
    example_2_start_present = {"by": By.XPATH, "value": "//*[@id='start']/button"}
    example_1_text = {"by": By.XPATH, "value": "//*[@id='finish']/h4"}
    example_2_text = {"by": By.XPATH, "value": "//*[@id='finish']/h4"}


    def click_example_1(self):
        self.click(self.example_1)

    def click_example_2(self):
        self.click(self.example_2)

    def example_1_start_button_present(self):
        return self.is_displayed(self.example_1_start_present)

    def example_2_start_button_present(self):
        return self.is_displayed(self.example_2_start_present)

    def example_1_start_button_click(self):
        self.click(self.example_2_start_present)

    def example_2_start_button_click(self):
        self.click(self.example_2_start_present)

    def example_1_text_present(self):
        self.click(self.example_1_text)

    def example_2_text_present(self):
        self.click(self.example_2_text)



