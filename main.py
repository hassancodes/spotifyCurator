import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint

# useless function
def func():
    print("\n")
    print("\n")
    print("\n")
    print("\n")

fb = "hassanhanjra900@gmail.com"
pw = 9018201778

driver = webdriver.Chrome('./chromedriver', keep_alive=True)
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fartists.spotify.com%2F")
time.sleep(4)

# driver.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/a").click()
time.sleep(4)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div/a").click()
time.sleep(4)
identer = driver.find_element_by_xpath("//*[@id='email']")
identer.send_keys(fb)
time.sleep(4)
passenter = driver.find_element_by_xpath("//*[@id='pass']")
passenter.send_keys(pw)

time.sleep(4)
login = driver.find_element_by_xpath("//*[@id='loginbutton']")
login.click();

time.sleep(4)

driver.get("https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/songs")
# musicbtn = driver.find_element_by_xpath("//a[@title='Music']")
time.sleep(4)
# musicbtn.click()
time.sleep(4)
playlist = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/section[1]/ul/li[3]/a")
playlist.click()

time.sleep(4)


# working  scroll feature



# searching for show more button.
driver.find_element_by_xpath("//*[contains(text(),'Show More')]").click()
print("Found the button")
time.sleep(4)

scroll = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/section[2]/div[4]/a")
scroll.send_keys(Keys.PAGE_DOWN)

func()
print(driver.get_cookies())
func()

# pprint.pprint(driver.page_source)
bod = driver.find_element_by_tag_name("body")
print(dir(bod))

func()
print(str(bod.text).encode())

# page source
# sourcepage = driver.getPageSource();
# print(sourcepage)
# working download
# downloadcsv = driver.get("https://artistinsights-downloads.spotify.com/v1/artist/7KzG8dszzwlSDGEsCbzANz/downloads/playlists.csv?time-filter=28day")






#####################################################################################














#####################################################################################
# with open("test.html","w") as fp:
#     fp.write(a)
#     print("saved")
# # pprint.pprint(res)
#
# time.sleep(5)
#
# driver.quit()


# add beautifulsoup to extract the playlist data and save it in a file.

print("Success you got it")
