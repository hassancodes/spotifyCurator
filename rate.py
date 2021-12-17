# this file return the $ rate of streams per
import pprint
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

cleanData = dict(OrderedDict())

# function to get the price per stream on spotify according to country place
def pps():

    url = "https://www.igroovemusic.com/blog/how-much-do-i-get-per-stream-on-spotify-2021-edition.html?lang=en"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    bod = soup.body
    rawdata = bod.find_all("tbody")[1]
    trdata = rawdata.find_all("tr")

    ls = ["Country" , "PPS","Per Million Streams", "Analysis","Change in %"]


    for tr in trdata :
        mydict = OrderedDict()
        counter =0
        for td in tr.find_all("td"):
            mydict[ls[counter]] = td.text

            counter +=1

        # print(mydict)
        cleanData[mydict["Country"]] = dict(mydict)

    return cleanData
