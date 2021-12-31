import json
import os


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
