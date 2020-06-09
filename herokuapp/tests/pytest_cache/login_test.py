import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService



class TestLogin():
    @pytest.fixture
    def driver(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome()
        else:
            driver_ = webdriver.Chrome()
        def quit():
            driver_.quit()
        request.addfinalizer(quit)
        return driver_

    #[Enter Correct Username and Password]
    def test_valid_credentials1(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("tomsmith")
        driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").is_displayed()

    #[Both Email and Password Fields are blank]
    def test_invalid_credentials2(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("")
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your username is invalid!\n×"

    #[Email field is filled and Password field is blank]
    def test_invalid_credentials3(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("tomsmith")
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your password is invalid!\n×"

    #[Email field is blank and Password field is filled]
    def test_invalid_credentials4(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("")
        driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your username is invalid!\n×"

    #[Email and Password are entered wrong]
    def test_valid_credentials5(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("tom")
        driver.find_element_by_id("password").send_keys("SuperSecret")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your username is invalid!\n×"

    #[Email is wrong and Password is correct]
    def test_valid_credentials6(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("tom")
        driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your username is invalid!\n×"

    #[Email is correct and Password is wrong]
    def test_valid_credentials7(self, driver):
        driver.get("http://the-internet.herokuapp.com/login")
        driver.find_element_by_id("username").send_keys("tomsmith")
        driver.find_element_by_id("password").send_keys("SuperSecret")
        driver.find_element_by_css_selector("button").click()
        assert driver.find_element_by_id("flash").text == "Your password is invalid!\n×"




