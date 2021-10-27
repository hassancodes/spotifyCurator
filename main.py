import time
import requests
import selenium
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pprint
import json

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

driver.implicitly_wait(3)


# working  scroll feature



# searching for show more button.
driver.find_element_by_xpath("//*[contains(text(),'Show More')]").click()
print("Found the button")
driver.implicitly_wait(3)

scroll = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/section[2]/div[4]/a")
scroll.send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(3)
func()
print(driver.get_cookies())
func()





driver.implicitly_wait(4)

func()
a = driver.find_element_by_tag_name("body")
soup  =BeautifulSoup(a.get_attribute("innerHTML"))
func()
# print(type(soup))
func()
bod = soup.body


fd = bod.find("div", {"id":"__next"})


# there are total three divs with the class name
MainDataDiv = fd.find_all("div", {"class": "styled__StyledSection-sc-1sttek1-0 dFCiJU"})

# varifying the length of divs
# print("LIST LENGTH : " ,len(MainDataDiv))
func()



tbody  = MainDataDiv[2].find("tbody")
# listeners, streams and are stored in

trList = tbody.find_all("tr")

dateList = tbody.find_all("td",{"class": "TableCell__TableCellElement-sc-1do596v-0 jdhnTQ SortTable__StyledTableCell-sc-4bygm5-1 jcBPas"})


func()
print(dateList)
func()


print(len(dateList))



# print("tr List:" , trList)

# trList[0].find_all("td")

# GOD FUNCTION
dictionary = {}
def createDict(ls):
    maindata = {"rank": "",
    "playlist Name": "",
    "No of Songs":"",
    "Curator" : "",
    "Listeners" : "",
    "Streams ":""}


    counter = 0
    for k,v in maindata.items():
        maindata[k] ="".join(ls[counter])
        counter +=1

    dictionary.update({maindata["playlist Name"] : maindata})


# function ends Here

# JSON DUMP function
def dumpjson(dict):
    with open("dump.json", 'w') as dj:
        # adding the generated data to json file
        json.dump(dict,dj)

# seperating title and

for i in trList:
    tdcounter = 0
    # [rank , PlaylistName , Number of songs, "curator" , "listeners" , "streams"]
    dataList = []
    for x in i.find_all("td"):

        if tdcounter == 1:

            print("test: ",x)
            pn = x.find("span").get_text()
            nos = x.find("h4").get_text()
            dataList.append(pn)
            dataList.append(nos)
        elif tdcounter == 2:
            curatorName  = "".join(x.get_text())
            dataList.append(curatorName)
        else:
            # the rest three data
            dataList.append(x.get_text())


        tdcounter+=1
        print("Data List: ", dataList)
    func()

    createDict(dataList)




pprint.pprint(dictionary)











# print("Length of playlists: ", len("tr"))









# print(dir(a))

func()



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
