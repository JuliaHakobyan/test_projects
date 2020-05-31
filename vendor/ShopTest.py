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
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]")).perform()
    time.sleep(3)
    previous_dress_name = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]/div/div[2]/h5/a").text
    print(previous_dress_name)
    previous_dress_price = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[6]/div/div[1]/div/div[2]/span").text
    print(previous_dress_price)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[7]")).perform()
    time.sleep(3)
    next_dress_name = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[7]/div/div[2]/h5/a").text
    print(next_dress_name)
    next_dress_price = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[7]/div/div[1]/div/div[2]/span[1]").text
    print(next_dress_price)
    time.sleep(3)

    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]")).perform()
    first_dress_name = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[2]/h5/a").text
    print(first_dress_name)
    first_dress_add = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[1]/div/div[2]/div[2]/a[1]/span").click()
    time.sleep(3)
    first_dress_view = driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span").click()
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]/span")).perform()
    first_dress_checkout = driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]/span").click()
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='create-account_form']")).perform()
    time.sleep(3)

    email_address = driver.find_element_by_id("email_create")
    email_address.clear()
    email_address.send_keys("hakobyan.julieta@yahoo.com")
    user_sign_up = driver.find_element_by_xpath("//*[@id='SubmitCreate']/span").click()
    time.sleep(3)




