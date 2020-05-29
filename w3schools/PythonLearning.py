from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
    time.sleep(3)
    start_python_class = driver.find_element_by_xpath('//a[@href="'+"python_intro.asp"+'"]').click()
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@href="'+"python_getstarted.asp"+'"]')).perform()
    time.sleep(3)
    next_lesson = driver.find_element_by_xpath('//a[@href="'+"python_getstarted.asp"+'"]').click()
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@href="'+"trypython.asp?filename=demo_helloworld"+'"]')).perform()
    time.sleep(3)
    try_yourself = driver.find_element_by_xpath('//a[@href="'+"trypython.asp?filename=demo_helloworld"+'"]').click()
    time.sleep(3)
    #text = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[2]/span")
    #text.clear()
    #time.sleep(5)
    #click_button = driver.find_element_by_xpath("/html/body/div[2]/div/button[2]").click()
    #time.sleep(3)
    #click_button = driver.find_element_by_css_selector("body > div.trytopnav > div > button.w3 - button.w3 - bar - item.w3 - green.w3 - hover - white.w3 - hover - text - green")
    #time.sleep(3)

    #try_yourself_close = driver.close()
    #driver.switch_to().python_get_started("Python Getting Started")
    #driver.find_element_by_xpath('//a[@href="'+"python_getstarted.asp"+'"]')
    #driver.switch_to_default_content()
    #time.sleep(3)

    driver.get("https://www.w3schools.com/python/python_getstarted.asp")
    time.sleep(3)
    driver.find_element_by_xpath('//a[@href="'+"python_syntax.asp"+'"]')
    time.sleep(3)
