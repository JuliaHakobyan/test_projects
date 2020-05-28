import driver as driver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome()


with Chrome() as driver:
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    url = driver.current_url
    title = driver.title
    print(title)
    print(url)

    #assert 'The Internet' in driver.title
    departments = driver.find_element_by_id("block_top_menu")
    #time.sleep(10)
    women_department = driver.find_element_by_class_name("sf-with-ul").click()
    time.sleep(5)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]")).perform()
    time.sleep(5)
    previous_dress = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]/div/div[2]/h5/a").text
    print(previous_dress)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[7]")).perform()
    time.sleep(5)
    next_dress = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[7]/div/div[2]/h5/a").text
    print(next_dress)
    time.sleep(5)