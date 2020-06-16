from selenium.webdriver.common.by import By
from new_project.w3schools.pages.basepage import BasePage


class PythonHomePage(BasePage):
    pythonHomePageTitle = {"by": By.XPATH, "value": "//*[@id='main']/h1"}
    homeButton = {"by": By.XPATH, "value": "//*[@id='main']/div[2]/a[1]"}
    nextButton = {"by": By.XPATH, "value": "//*[@id='main']/div[2]/a[2]"}
    startLearningPythonButton = {"by": By.XPATH, "value": "//*[@id='main']/div[3]/a"}
    exampleText = {"by": By.XPATH, "value": "//*[@id='main']/div[4]/div"}
    tryItYourselfButton = {"by": By.XPATH, "value": "//*[@id='main']/div[4]/a"}


    def __init__(self, driver):
        super().__init__(driver)
        self.visit("https://www.w3schools.com/python/default.asp")
        assert self.is_displayed(self.pythonHomePageTitle)

    def click_start_learning_python(self):
        return self.is_displayed(self.)








