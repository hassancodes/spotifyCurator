import flask
from flask import *
import json
from collections import OrderedDict
from rate import pps
from helpfunc import displaylists, get_index,displayppt
from helpfunc import get_indexppt
from helpfunc import getplaylistname, blacklistus
from dbhandle import dbfetch
import os

application = Flask(__name__)


############################### Opening data files here to create variable for templates ######################
file = open("scrapejson/tedays.json", "r", encoding="utf-8")
jData = json.load(file)

# sd is sevenday file
sdfile = open("scrapejson/sevendays.json", "r", encoding="utf-8")
sdData = json.load(sdfile)
# print(jData)

tffile = open("scrapejson/tfhours.json", "r", encoding="utf-8")
tfData = json.load(tffile)






# Home Route
ab = "tutorial"
@application.route("/")
def main():
    return render_template("index.html" , jData=jData, var=ab)

###############################################GOD Function ########################################################
# handling the add playlist submission data
@application.route('/handle_data', methods=['POST'])
def handle_data():
    # this is the current data the user will input
    index = get_index()
    data = {
    "id" : index+1,
    "amount_paid":request.form["amount_paid"],
    "playlistlink":request.form["playlistlink"],
    "insta": request.form["insta"],
    "noofsongs": request.form["noofsongs"],
    "noofplaylist": request.form["noofplaylist"],
    "country":request.form['country'],
    "start_date":request.form["start_date"],
    "end_date":request.form["end_date"]
    }

    with open("addplaylist.json" , "r+") as file:

        # working on presistent data in add playlist.json
        mydict = OrderedDict()
        ls = []
        jsonsize = os.path.getsize("addplaylist.json")
        if jsonsize ==0:
            ls.append(data)
            mydict["PlayList Data"] = ls
            json.dump(mydict,file)
            # changed
            return redirect(url_for("addplaylist"))
        elif jsonsize!=0:

            file_data = json.load(file)
            file_data["PlayList Data"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

# redirecting after adding the data to the form
    return redirect(url_for("addplaylist"))


#######################################################################################################
# # handling the submission of potential PlayList
@application.route("/handle_ppt", methods=['POST'])
def handle_ppt():

    index =get_indexppt()
    file_loc = "maindata/potentialplaylists.json"
    data = {
        "id" : index+1 ,
        "Amount" : request.form["amount"],
        "location" : request.form["location"],
        "playlist link" : getplaylistname(request.form["playlistlink"]),
        "curator contact" : request.form["curatorcontact"]
        }

    with open(file_loc , "r+") as ppt:
        # working on presistent data in add playlist.json
        mydict = OrderedDict()
        ls = []
        jsonsize = os.path.getsize(file_loc)
        if jsonsize ==0:
            ls.append(data)
            mydict["Potential Playlists"] = ls
            json.dump(mydict,ppt)
            # changed
            return redirect(url_for("pplaylists"))
        elif jsonsize!=0:

            file_data = json.load(ppt)
            file_data["Potential Playlists"].append(data)
            ppt.seek(0)
            json.dump(file_data,ppt, indent = 4)

    # redirecting after adding the data to the form
    return redirect(url_for("pplaylists"))




# this blacklist handle
@application.route("/handle_blacklist", methods=["POST"])
def handle_blacklist():
    data_dict = {}
    link = request.form["blacklist"]

    bljson  = blacklistus("iamdope",link)
    return redirect("/blacklist")



# actual blacklist endpoint
var = "main"
@application.route("/blacklist")
def blacklist():
    data = dbfetch("miscellaneous", "blacklist")
    # list that contains all the clean dictionaries
    mainlist = []
    if len(data) <1:
        pass
    else:
        # setting the counter so we can go through all the item
        outcounter = 0
        for dictionary in data:
            counter = 0
            ownername = [k for k,v in data[outcounter].items()][0]
            # print("ownerbooks" ,ownername)
            for items in range(len(data[outcounter][ownername]["items"])):
                singDict = {}
                # getting the owner name to call data
                singDict["plname"]    = dictionary[ownername]["items"][counter]["name"]
                singDict["pllink"]    = dictionary[ownername]["items"][counter]["external_urls"]["spotify"]
                singDict["ownername"] = dictionary[ownername]["items"][counter]["owner"]["display_name"]
                singDict["ownerlink"] = dictionary[ownername]["items"][counter]["owner"]["external_urls"]["spotify"]
                try:
                    singDict["imagesrc"]  = dictionary[ownername]["items"][counter]["images"][0]["url"]
                except IndexError:
                    singDict["imagesrc"]  = "https://images.pexels.com/photos/167092/pexels-photo-167092.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                # print("counter",counter)
                mainlist.append(singDict)
                counter +=1
            outcounter +=1
        print("length of main list" ,len(mainlist))
        return render_template("blacklist.html",dbdata=mainlist, var=var)


#############################seven days endpoint #################################
@application.route("/sevendays")
def seven_days():
    return render_template("sevendays.html" ,sdData =sdData)

##############################24 hours end point######################################
@application.route("/24hours")
def tf_hours():
    return render_template("tfhours.html" ,tfData =tfData)

# Work Here

# this the main functionality endpoint.(Adds data)
var = "main"
@application.route("/addplaylists")
def addplaylist():
    pldata = displaylists()
    return render_template("addplaylists.html", var=var,pldata=pldata)


# Seperate script for checking potential playlists.
var = "main"
@application.route("/potentialplaylists")
def pplaylists():
    pptdata  = displayppt()
    return render_template("potentialplaylists.html", pptdata = pptdata ,var=var)


var = "main"
ratepps = pps()
data = dict(ratepps)
@application.route("/ratepps")
def ratepps():
    return render_template("rate.html", data=data, var =var)







#################################### Endpoints below require more work ########################################
# miscellaneous
# about, main
var = "main"
@application.route("/tutorial")
def tut():
    return render_template("tutorial.html", var=var)



@application.route("/login")
def login():
    return render_template("login.html")


# function to display error pages
@application.route("/<random>")
def error(random):
    return "Page not found!"

if __name__ == "__main__":
    application.run()
