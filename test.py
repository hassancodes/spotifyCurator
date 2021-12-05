import time
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from collections import OrderedDict
import pprint
import json
import random


# op = Options()
# op.add_experimental_option("excludeSwitches", ["enable-automation"])
# op.add_experimental_option('useAutomationExtension', False)
# op.add_argument("start-maximized")
driver = webdriver.Chrome()
# driver = webdriver.Chrome('./chromedriver', options=op)
driver.get("https://google.com/")
time.sleep(4)
