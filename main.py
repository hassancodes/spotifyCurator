import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint

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
# playlist = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/section[1]/ul/li[3]/a")
# playlist.click()


# time.sleep(4)

# working download
# downloadcsv = driver.get("https://artistinsights-downloads.spotify.com/v1/artist/7KzG8dszzwlSDGEsCbzANz/downloads/playlists.csv?time-filter=28day")

res = requests.get("https://generic.wg.spotify.com/s4x-insights-api/v1/artist/7KzG8dszzwlSDGEsCbzANz/playlists/listener?time-filter=28day")
# res = requests.get("https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/playlists/listener?time-filter=28day")

# print(type(res.json()))
print(res.status_code)
pprint.pprint(res.content)
# str(res.content)

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
