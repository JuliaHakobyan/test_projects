import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from herokuapp.pages import base_page
from herokuapp.pages import authorization_page


class TestLogout:
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
        return authorization_page.AuthorizationPage(driver_)

    def logout(self, driver):
        self.is_displayed(self.login_form)
        self.click(self.logout_button)
        assert self.is_displayed(self.logout_success_message_present())
