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

# def blacklistus(link):
#     user = link.split("/")[-1]
#     # mainurl = f"https://spclient.wg.spotify.com/user-profile-view/v3/profile/{user}?playlist_limit=10&artist_limit=10&market=from_token"
#     mainurl = link
#     headers ={
#         "accept": "application/json",
#         "accept-language": "en",
#         "app-platform": "WebPlayer",
#         "cache-control": "no-cache",
#         "pragma": "no-cache",
#         "sec-ch-ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "spotify-app-version": "1.1.77.277.g27ca9e7b",
#         "Referer": "https://open.spotify.com/",
#         "Referrer-Policy": "strict-origin-when-cross-origin"
#       }
#           # "authorization": "Bearer BQDrzoZxnnqBcvB5qUweoG9pbKyY-2Gt6je7yci8MuYQG0fZSfBCGEnjthy3cdMtlfT2auShMldcl0t4lkYFBgsvrhLJBYBzYe3XD7proBFufMZSkPj3Bvm_s6Rvr-hVq7vMUHLJ-RoUYepxbESqG7o0VQikwdZ_6zK4q2vkpu9kywuUOu1kootB2JF0iGU0_zEpaX5eHOaWd3cB9Ye0GEStEMpGrNZVlHtOyX3RW9sYR-2HG4mlR-KvSxzjbR5UV3QVSWkaiMaxsEGrodPu0mZ7HukRxlO7ddQFsFmbHXF_pqBzqHaBI6Vf",
#     req = requests.get(mainurl, headers=headers)
#     # a = str(req.json()).replace("'" , '"')
#     # soup = BeautifulSoup(req.content, 'lxml')
#     # blackdata = soup.body.get_text()
#     # pprint.pprint(blackdata)
#     print(a)

# blacklistus("https://open.spotify.com/user/1186336261")
# getplaylistname("https://open.spotify.com/playlist/0HtZSEqRMz6L5ZXAWCBgWp")


############################ get the function ##############################
# this returns the playlist data based on


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
