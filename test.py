import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver', keep_alive=True)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
time.sleep(4)

html = driver.find_element_by_class_name("extiw")

html.send_keys(Keys.PAGE_DOWN)
