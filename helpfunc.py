import pprint
import json
import os
import requests
from bs4 import BeautifulSoup


# this functions helps in displaying the added playlist.
def displaylists():
    file_loc  = "addplaylist.json"
    filesize = os.path.getsize(file_loc)
    if filesize == 0 :
        return {}
    else:
        with open(file_loc, 'r') as  file:
            data = json.loads(file.read())
            if len(data)<1:
                return {}
            else:
                return data["PlayList Data"]
# print(displaylists())
####################################################################################



def displayppt():
    file_loc  =  "maindata/potentialplaylists.json"
    exist = os.path.exists(file_loc)
    if exist == False:
        with open(file_loc, "r+") as file:
            pass
    elif exist==True:
        filesize = os.path.getsize(file_loc)
        if filesize == 0 :
            return {}
        else:
            with open(file_loc, 'r') as  file:
                data = json.loads(file.read())
                if len(data)<1:
                    return {}
                else:
                    return data["Potential Playlists"]

# print(displayppt())


####################################################################################


# this functions returns the index for the row we are adding
def get_index():
    with open("addplaylist.json", 'r') as js:
        data = json.loads(js.read())
        return len(data["PlayList Data"])


####################################################################################
def get_indexppt():
    file_loc  =  "maindata/potentialplaylists.json"
    filesize = os.path.getsize(file_loc)
    if filesize == 0:
        return 0
    else:
        with open(file_loc, 'r') as js:
            data = json.loads(js.read())
            return len(data["Potential Playlists"])


####################################################################################

def getplaylistname(link):
    headers = {
    "accept-language": "en",
     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4818.2 Safari/537.36"

    }
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.content, "lxml")

    title = str(soup.find("title").get_text()).split("- playlist by")[0]
    return title.strip()




####################################################################################
def fetchdata(noofdays):
    if noofdays == 7:
        dbname = client["spotifyCurator"]
        sevendays = dbname["sevendayscol"]
        data = dict(list(sevendays.find_one().items())[1:])
        return data

    elif noofdays == 28:
        dbname = client["spotifyCurator"]
        tedays = dbname["tedayscol"]
        data = dict(list(tedays.find_one().items())[1:])
        return data


    elif noofdays ==24:
        dbname = client["spotifyCurator"]
        tfhours = dbname["tfhourscol"]
        data = dict(list(tfhours.find_one().items())[1:])
        return data
