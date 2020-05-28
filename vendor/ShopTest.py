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
    #time.sleep(10)
    #product_list = driver.find_elements_by_class_name("product_list grid row")
    #time.sleep(10)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]")).perform()
    time.sleep(10)
    previous_dress = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]/div/div[2]/h5/a").text
    print(previous_dress)
    #time.sleep(10)
    #next_dress = driver.find_element_by_xpath("//*[@id=center_column]/ul/li[7]/div/div[1]/div/a[1]/img")
    #next_dress = driver.find_element_by_xpath("//*[@id=center_column]/ul/li[7]/div/div[1]/div/a[1]/img").getText("text")




    #login_field = driver.find_element_by_id("username")
    #login_field.send_keys("tomsmith")
    #password_field = driver.find_element_by_id("password")
    #password_field.send_keys("SuperSecretPassword!" + Keys.ENTER)