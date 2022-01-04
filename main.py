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


driver=None
# useless function
def func():
    print("\n \n \n \n")
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
            # print(ls)
            # print(len(ls))
        counter +=1

    if maindata["playlistname"] == "Unknown":
        dictionary.update({maindata["playlistname"]+f"{random.randint(1,100)}" : maindata})
    elif maindata["playlistname"] != "Unknown":
        dictionary.update({maindata["playlistname"] : maindata})


################################### for dumping #############################

def dumpjson(dict,filename):
    with open(f"scrapejson/{filename}.json", 'w', encoding="utf-8") as dj:
        # adding the generated data to json file
        json.dump(dict,dj)


################################## MAIN FUNCTION ##########################################
def main(email,pw,loginOpt):


    op = Options()
    op.add_argument('--headless')
    op.add_argument("window-size=1920,1080")
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("start-maximized")

    global driver
    driver = webdriver.Chrome('./chromedriver', options=op)
    print(driver.get_window_size())
    driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fartists.spotify.com%2F")
    time.sleep(4)

    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/a").click()

    # for users that login with facebook API
    if loginOpt==1:

        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div/a").click()
        time.sleep(4)
        identer = driver.find_element_by_xpath("//*[@id='email']")
        identer.send_keys(email)
        time.sleep(4)
        passenter = driver.find_element_by_xpath("//*[@id='pass']")
        passenter.send_keys(pw)
        time.sleep(4)
        login = driver.find_element_by_xpath("//*[@id='loginbutton']")
        login.click();
    # for users that uses email to login to spotify for artists.
    elif loginOpt ==2:
        # Still need to figure this out
        print("GOOGLE")

    elif loginOpt ==3:
        print("APPLE")
    elif loginOpt==4:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.implicitly_wait(4)
        identer = driver.find_element_by_xpath('//*[@id="login-username"]')
        identer.send_keys(email)
        driver.implicitly_wait(3)
        passenter = driver.find_element_by_xpath('//*[@id="login-password"]')
        passenter.send_keys(pw)
        driver.implicitly_wait(3)
        login = driver.find_element_by_xpath('//*[@id="login-button"]')
        login.click();



    time.sleep(10)
# from here the process is same for all login
    driver.get("https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/songs")
    # musicbtn = driver.find_element_by_xpath("//a[@title='Music']")
    time.sleep(4)

    # this get the 28 days data
    # /html/body/div[2]/div/div/div/div/div/main/div/div/div/div[2]/section[1]/ul/li[3]/a
    playlist = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/main/div/div/div/div[2]/section[1]/ul/li[3]/a")
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
    mbody = BeautifulSoup(tedays.get_attribute("innerHTML"), "lxml")
    # # I already got the 28 days data which is stored in body variables.
    # Now I will target the 7 day link and store that body of that page
    driver.implicitly_wait(10)

############################Fetching Seven days data######################################
    # getting the seven days data.
    driver.get("https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/playlists?time-filter=7day")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("worked")
    driver.implicitly_wait(4)
    # searching for show more button.
    driver.find_element_by_xpath("//*[contains(text(),'Show More')]").click()
    print("Found the button")
    driver.implicitly_wait(4)
    func()
    sevendays = driver.find_element_by_tag_name("body")
    sebody = BeautifulSoup(sevendays.get_attribute("innerHTML"), "lxml")

    # add in data to html file
    with open("scrapehtml/sevendays.html", "w",encoding="utf-8") as file:
        file.write(f"{sebody}")
        print("Successfully data written to sevendays.html")

############################24 days data######################################
    # getting the seven days data.
    driver.get("https://artists.spotify.com/c/artist/7KzG8dszzwlSDGEsCbzANz/music/playlists?time-filter=1day")
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("worked")
    driver.implicitly_wait(4)
    # searching for show more button.
    driver.find_element_by_xpath("//*[contains(text(),'Show More')]").click()
    print("Found the button")
    driver.implicitly_wait(4)
    func()
    tfhours = driver.find_element_by_tag_name("body")
    tfbody = BeautifulSoup(tfhours.get_attribute("innerHTML"), "lxml")

    # add in data to html file
    with open("scrapehtml/tfhours.html", "w",encoding="utf-8") as file:
        file.write(f"{tfbody}")
        print("Successfully data written to tfhours.html")

# ###################################Seven days fetching ends here###############################
#
    return mbody

#################################### ADDing to HTML FILE ###################################

def addtoHtml():

    # adding multiple login functionality.
    print("Choose login options that you use for spotify for artists: \n1.)Facebook \n2.)Google \n3.)Apple \n4.)Email")
    loginOpt = int(input())
    print("Enter Email:")
    email =input()
    print("Enter Password:")
    pw = input()

    body = main(email,pw, loginOpt)
    # mbody = BeautifulSoup(body.get_attribute("innerHTML"), "lxml")

    # add in data to html file
    with open("scrapehtml/tedays.html", "w",encoding="utf-8") as file:
        file.write(f"{body}")
        print("Successfully data written to tedays.html")


############################### Parsing the html file ###########################################
def parsefunc(filename):
    with open(f"scrapehtml/{filename}.html", "r", encoding="utf-8") as rfile:
        rbody=BeautifulSoup(rfile.read() , "lxml")
        # there are total 3 sections in the html.  and two tbodys with the required data.
        trList = rbody.find_all("section")[2].find_all("tbody")[1].find_all("tr")
        # trList  = [x.prettify().encode('utf8').decode('ascii', 'ignore') for x in rtList]
        # print(trList)

        print(len(trList))
        # print(trList[0])
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
        dumpjson(dictionary,filename)

# main logic starts from here
addtoHtml()
time.sleep(10)
parsefunc("tedays")
time.sleep(10)
# print(pprint.pprint(dictionary))

######################################seven days creating json ########################################
# initializing the dictionary again to store the seven data from start
dictionary = OrderedDict()
time.sleep(10)
parsefunc("sevendays")
time.sleep(10)
# print(pprint.pprint(dictionary))


######################################24 hours creating json ########################################
# initializing the dictionary again to store the seven data from start
dictionary = OrderedDict()
time.sleep(10)
parsefunc("tfhours")
time.sleep(10)
# print(pprint.pprint(dictionary))





#####################################################################################
print("Success you got it")
time.sleep(10)
driver.close()
