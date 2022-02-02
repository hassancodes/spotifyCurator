import pprint
import json
import os
import requests
from bs4 import BeautifulSoup
from spotipy import util
from bs4 import BeautifulSoup
import pprint
# non-native functions
from dbhandle import dbinsert


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



############################# Function for blacklisting #####################################
#  this function use spotify api to generate a accesstoken and
# then uses that token to fetch the users playlists to blacklist
# First the data is stored in a db and then the blacklist functions fetches the data from mongodb for front
def blacklistus(user,prof_link):
    profile = None
    # validating the link
    if prof_link.startswith("https://open.spotify.com/user/") or prof_link.startswith("open.spotify.com/user/"):
        profile = prof_link.split("/")[-1]
        token = util.prompt_for_user_token(user,client_id='f198005bb50e43ffae25db4194603bad',client_secret='3e8d3b3c68464b2a91cf753950245148',redirect_uri="http://127.0.0.1:5000/callback")
        # print(token)

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Host": "api.spotify.com",
        }

        params = {
        "offset": 0,
        "limit" : 20
        }

        tar_url  = f"https://api.spotify.com/v1/users/{profile}/playlists"
        # sending the final request
        req = requests.get(tar_url, headers=headers, params=params)
        # soup = BeautifulSoup(data.content,"lxml")
        # value = eval(str(req.json()).replace("'", '"'))
        value = req.json()
        key = value["items"][0]["owner"]["display_name"]
        #
        mydict = { key : value }
        data = mydict
        # # using the universal dbinsert function
        dbinsert("miscellaneous","blacklist",mydict)
        # return data[key]

    else:
        return "invalid Profile Link"




blacklistus("iamdope","https://open.spotify.com/user/e5kzgfyenbpthi0ew37kmrgmq")
