from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome()
with Chrome() as driver:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.maximize_window()
    url = driver.current_url
    title = driver.title
    print(title)
    print(url)
    print(url)
    print(url)
    print(url)
    print(url)

    assert 'The Internet' in driver.title
    login_field = driver.find_element_by_id("username")
    login_field.send_keys("tomsmith")
    password_field = driver.find_element_by_id("password")
    password_field.send_keys("SuperSecretPassword!" + Keys.ENTER)