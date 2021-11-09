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


    counter = -1
    for k,v in maindata.items():
        counter +=1
        if counter ==7:
            maindata[k] = round((int(maindata["streams"].replace(",",'')) * 0.006),2)
        else:
            maindata[k] ="".join(ls[counter])

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
    body = driver.find_element_by_tag_name("body")

    return body

#################################### ADDing to HTML FILE ###################################

def addtoHtml():
    fb = "hassanhanjra900@gmail.com"
    pw = 9018201778

    body = main(fb,pw)
    mbody = BeautifulSoup(body.get_attribute("innerHTML"), "lxml")

    # add in data to html file
    with open("data.html", "w",encoding="utf-8") as file:
        file.write(f"{mbody}")
        print("Successfully data written to data.html")


############################### Parsing the html file ###########################################
def parsefunc():

    with open("data.html", "r", encoding="utf-8") as rfile:
        rbody=BeautifulSoup(rfile.read() , "lxml")

        # there are total 3 sections in the html.  and two tbodys with the required data.
        trList = rbody.find_all("section")[2].find_all("tbody")[1].find_all("tr")
        # trList  = [x.prettify().encode('utf8').decode('ascii', 'ignore') for x in rtList]

        print(len(trList))
        for i in trList:
            tdcounter = 0
            # [rank , PlaylistName , Number of songs, "curator" , "listeners" , "streams"]
            dataList = []
            for x in i.find_all("td"):
                if tdcounter == 1:
                    # print("test: ",x)
                    pn = x.find("span").get_text()
                    nos = x.find("h4").get_text()
                    dataList.append("".join(pn))
                    dataList.append("".join(nos))
                elif tdcounter == 2:
                    curatorName  = "".join(x.get_text())
                    dataList.append(curatorName)
                else:
                    # the rest three data
                    dataList.append(x.get_text())


                tdcounter+=1
                # print("Data List: ", dataList)

            createDict(dataList)

        dumpjson(dictionary)




# main logic
addtoHtml()
parsefunc()



































    # life saviour line 105
    # prettify().encode('utf8').decode('ascii', 'ignore')
    # with open("lol.html", "w" ,encoding="utf-8") as lo:
    #     lo.write(f"{div}")




# fd = bod.find("div", {"id":"__next"})
# # print("fd : ",fd)
#
# # there are total three divs with the class name
# ################# Needs to be updated (spotify for artists changes classes over time)
# MainDataDiv = fd.find_all("div", {"class": "styled__StyledSection-sc-1sttek1-0 fCPWQo"})
# print("Main Data Div: ", len(MainDataDiv))

# # varifying the length of divs
# # print("LIST LENGTH : " ,len(MainDataDiv))
# func()
# # print(MainDataDiv)
#
#
#
# tbody  = MainDataDiv[2].find("tbody")
# # listeners, streams and are stored in
# print("Maindatadiv[]: ", MainDataDiv)
# trList = tbody.find_all("tr")
# print("TRLIST:" ,len(trList))
#
# ############## Needs to be updated (spotify for artists changes classes over time)
# dateList = tbody.find_all("td",{"class": "TableCell__TableCellElement-sc-1do596v-0 huXJQd SortTable__StyledTableCell-sc-4bygm5-1 XvWyE"})
#
#
# func()
#
# print(dateList)
#
# func()
#
#
# print(len(dateList))
#
#
#
# # print("tr List:" , trList)
#
# # trList[0].find_all("td")
#

#
# # function ends Here
#
# # JSON DUMP function
#
# # seperating title and
# # this function iterates over the list
# for i in trList:
#     tdcounter = 0
#     # [rank , PlaylistName , Number of songs, "curator" , "listeners" , "streams"]
#     dataList = []
#     for x in i.find_all("td"):
#         if tdcounter == 1:
#             print("test: ",x)
#             pn = x.find("span").get_text()
#             nos = x.find("h4").get_text()
#             dataList.append("".join(pn))
#             dataList.append(nos)
#         elif tdcounter == 2:
#             curatorName  = "".join(x.get_text())
#             dataList.append(curatorName)
#         else:
#             # the rest three data
#             dataList.append(x.get_text())
#
#
#         tdcounter+=1
#         print("Data List: ", dataList)
#     func()
#
#     createDict(dataList)
# #
# #
# #
# # # dumping the end json into the file
# dumpjson(dictionary)
# print("exiting... chrome")
# time.sleep(3)
# driver.quit()
#









# print("Length of playlists: ", len("tr"))









# print(dir(a))

# func()



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
