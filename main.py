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

# useless function
def func():
    print("\n")
    print("\n")
    print("\n")
    print("\n")

################################### # GOD FUNCTION##############################

dictionary = OrderedDict()
def createDict(ls):
    maindata = {"rank": "",
    "playlistname": "",
    "noofsongs":"",
    "curator" : "",
    "listeners" : "",
    "streams":"",
    "date": "",
    "revenue": ""
    }


    counter =0
    for k,v in maindata.items():
        if counter ==7:
            maindata[k] = round((int(maindata["streams"].replace(",",'')) * 0.006),2)
        else:
            maindata[k] ="".join(ls[counter])
        counter +=1

    if maindata["playlistname"] == "Unknown":
        dictionary.update({maindata["playlistname"]+f"{random.randint(1,10)}" : maindata})
    elif maindata["playlistname"] != "Unknown":
        dictionary.update({maindata["playlistname"] : maindata})


################################### for dumping #############################

def dumpjson(dict):
    with open("dump.json", 'w', encoding="utf-8") as dj:
        # adding the generated data to json file
        json.dump(dict,dj)


################################## MAIN FUNCTION ##########################################
def main(fb,pw):

    op = Options()
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("start-maximized")


    driver = webdriver.Chrome('./chromedriver', keep_alive=True, options=op)
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
    # time.sleep(4)
    playlist = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/main/div/div/div/div[2]/section[1]/ul/li[3]/a")
    playlist.click()

    driver.implicitly_wait(4)

    # working  scroll featur
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.implicitly_wait(4)

    # searching for show more button.
    driver.find_element_by_xpath("//*[contains(text(),'Show More')]").click()
    print("Found the button")
    driver.implicitly_wait(4)
    func()
    # twentyeightdays = tedays
    tedays = driver.find_element_by_tag_name("body")
    # # I already got the 28 days data which is stored in body variables.
    # Now I will target the 7 day link and store that body of that page
    return tedays
#################################### ADDing to HTML FILE ###################################

def addtoHtml():
    fb = "hassanhanjra900@gmail.com"
    pw = 9018201778

    body = main(fb,pw)
    mbody = BeautifulSoup(body.get_attribute("innerHTML"), "lxml")

    # add in data to html file
    with open("tedays.html", "w",encoding="utf-8") as file:
        file.write(f"{mbody}")
        print("Successfully data written to data.html")


############################### Parsing the html file ###########################################
def parsefunc():

    with open("tedays.html", "r", encoding="utf-8") as rfile:
        rbody=BeautifulSoup(rfile.read() , "lxml")

        # there are total 3 sections in the html.  and two tbodys with the required data.
        trList = rbody.find_all("section")[2].find_all("tbody")[1].find_all("tr")
        # trList  = [x.prettify().encode('utf8').decode('ascii', 'ignore') for x in rtList]

        print(len(trList))
        print(trList[0])
        for i in trList:
            tdcounter = 0
            # [rank , PlaylistName , Number of songs, "curator" , "listeners" , "streams", "date"]
            dataList = []
            data = i.find_all("td")
            for x in range(len(data)):

                if x == 1:
                    # print("test: ",x)
                    pn = "Unknown"  if data[x].find("span").get_text()=="" else data[x].find("span").get_text()
                    nos = data[x].find("h4").get_text()
                    dataList.append("".join(pn))
                    dataList.append("".join(nos))
                elif x == 2:
                    curatorName  = "".join(data[x].get_text())
                    dataList.append(curatorName)
                else:
                    # the rest three data
                    dataList.append(data[x].get_text())
                # tdcounter+=1
                # print("Data List: ", dataList)

            createDict(dataList)
            print("1:",dictionary)
        dumpjson(dictionary)




# main logic starts from here
addtoHtml()
parsefunc()

#####################################################################################
print("Success you got it")
