import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from new_project.herokuapp.pages.secure_page import SecurePage

class TestLogin():
    @pytest.fixture
    def driver(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = ChromeService(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()
        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return SecurePage(driver_)


    def test_succes_login_logout(self, driver):
        driver.with_("tomsmith", "SuperSecretPassword!")
        assert (driver.login_success_message_present())

        driver.close_login_message()
        driver.click(driver.login_success_message_close)

        driver.logout()
        assert (driver.logout_success_message_present())
