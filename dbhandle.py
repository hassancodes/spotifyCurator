import pymongo
from pymongo import MongoClient
import urllib

# Creating and instance of MongoClient
# client= MongoClient(host="localhost", port=27017)
# tfhoursdb = client.tfhours
# sevendaysdb = client.sevendays
# tedaysdb = client.tedays
#
# print(client.list_database)
username = "muhammadhassan"
password = "mongodbevjr3303@A"
client = MongoClient("mongodb+srv://muhammadhassan:" + urllib.parse.quote("mongodbevjr3303@A") + "@cluster0.tsgul.mongodb.net/testdatabase?retryWrites=true&w=majority")
dbname = client["spotifyCurator"]


collection_name = dbname["tfhourscol"]


item_1 = {

"lol" : "dope"
}


collection_name.insert_one(item_1)

print(collection_name)
