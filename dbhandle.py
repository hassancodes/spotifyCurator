import pymongo
from pymongo import MongoClient
import urllib
import json
from decouple import config
from datetime import datetime


userID = config('id',default='')
password = config('password',default='')
client = MongoClient("mongodb+srv://muhammadhassan:" + urllib.parse.quote("mongodbevjr3303@A") + "@cluster0.tsgul.mongodb.net/testdatabase?retryWrites=true&w=majority")

def dbhandle():
    dbname = client["spotifyCurator"]


    tfhours = dbname["tfhourscol"]
    sevendays = dbname["sevendayscol"]
    tedays = dbname["tedayscol"]


    with open("scrapejson/tfhours.json" ,"r") as tf:
        tfdata = json.loads(tf.read())
        tfhours.delete_many({})
        tfhours.insert_one(tfdata)
        # tfhours.insert_one(tfdata)

    with open("scrapejson/tedays.json" ,"r") as te:
        tedata = json.loads(te.read())
        tedays.delete_many({})
        tedays.insert_one(tedata)


    with open("scrapejson/sevendays.json" ,"r") as sd:
        sdData = json.loads(sd.read())
        sevendays.delete_many({})
        sevendays.insert_one(sdData)


# this function stores the 24 hours data on regular basics
def longTermData():
    # for now just storing the 24 data, because we can use that to generate 7day and 28 day data
    dbname = client["spotifyCuratorExtra"]

    # collection inside dbname
    tfhours = dbname["tfhourslong"]
    # sevendays = dbname["sevendayslong"]
    # tedays = dbname["tedayslong"]
    currentDate = curdate()
    with open("scrapejson/tfhours.json" ,"r") as tf:
        tfdata = json.loads(tf.read())
        tfhours.insert_one({ currentDate : tfdata})






def curdate():
    year = datetime.now().year
    day = datetime.now().day
    month = datetime.now().month

    x =datetime(year,month,day)
    return x.strftime("%b %d %Y")


# main call start fron here
longTermData()
