from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = Chrome

with Chrome() as driver:
    driver.get("https://www.w3schools.com/")
    driver.maximize_window()
    url = driver.current_url
    title = driver.title
    print(title)
    print(url)

    #ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@href="'+"/python/default.asp"+'"]')).perform()
    select_python_class = driver.find_element_by_xpath('//a[@href="'+"/python/default.asp"+'"]').click()
    time.sleep(2)
    start_python_class = driver.find_element_by_xpath('//a[@href="'+"python_intro.asp"+'"]').click()
    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@href="'+"python_getstarted.asp"+'"]')).perform()
    time.sleep(2)
    next_lesson = driver.find_element_by_xpath('//a[@href="'+"python_getstarted.asp"+'"]').click()
    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@href="'+"trypython.asp?filename=demo_helloworld"+'"]')).perform()
    time.sleep(2)
    try_yourself = driver.find_element_by_xpath('//a[@href="'+"trypython.asp?filename=demo_helloworld"+'"]').click()
    time.sleep(5)
    text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[2]/span")
    text.clear()
    #time.sleep(5)

    #ActionChains(driver).move_to_element(driver.find_element_by_css_selector("#mySidenav > div > a:nth-child(26)")).perform()
    #time.sleep(3)
    #driver.find_element_by_