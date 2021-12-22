import json
import os


# this functions helps in displaying the added playlist.
def displaylists():
    filesize = os.path.getsize("addplaylist.json")
    if filesize == 0 :
        return {}
    else:
        with open("addplaylist.json", 'r') as  file:
            data = json.loads(file.read())
            if len(data)<1:
                return {}
            else:
                return data["PlayList Data"]
# print(displaylists())
