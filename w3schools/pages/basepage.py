from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, input_text):
        self.find(locator).send_keys(input_text)

    def is_displayed(self, locator, tomeout=0):
        if tomeout > 0:
            try:
                wait = WebDriverWait(self.driver, tomeout)
                wait.until(expected_conditions.visibility_of_element_located(
                        (locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self.find(locator).is_displayed()
            except NoSuchElementException:
                return False