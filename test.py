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

def bl():
    token = util.prompt_for_user_token("iamdope",client_id='f198005bb50e43ffae25db4194603bad',client_secret='3e8d3b3c68464b2a91cf753950245148',redirect_uri="http://127.0.0.1:5000/callback")
    # print(token)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}",
    }

    # params = {
    # "offset": 0,
    # "limit" : 20
    # }

    tar_url  = f"https://open.spotify.com/artist/0X3nsc84A9qlFilmlWNwQb/discovered-on"
    # sending the final request
    req = requests.get(tar_url, headers=headers)
    print(req.content)

bl()
