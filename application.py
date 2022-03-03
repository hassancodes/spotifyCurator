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


################################################ GLOBAL VARIABLES ###############################################
countrylist = []




############################### Opening data files here to create variable for templates ######################
file = open("scrapejson/tedays.json", "r", encoding="utf-8")
jData = json.load(file)

# sd is sevenday file
sdfile = open("scrapejson/sevendays.json", "r", encoding="utf-8")
sdData = json.load(sdfile)
# print(jData)

tffile = open("scrapejson/tfhours.json", "r", encoding="utf-8")
tfData = json.load(tffile)

#all time data
alltimefile = open("scrapejson/alltime.json", "r", encoding="utf-8")
alltimeData = json.load(alltimefile)





# Home Route

@application.route("/")
def main():
    return render_template("index.html" , jData=jData)

###############################################GOD Function ########################################################
# handling the add playlist submission data
@application.route('/handle_data', methods=['POST'])
def handle_data():
    # this is the current data the user will input
    index = get_index()
# using the help function that will retrieve us the playlist name

    playlist_name = getplaylistname(request.form["playlistlink"])
    playlist_link = request.form["playlistlink"]
    print("PLaylist Name" , playlist_name)


    data = {
    "id" : index+1,
    "amount_paid":request.form["amount_paid"],
    "playlistlink":{
        "link" : playlist_link,
        "name" : playlist_name
    },
    "insta": request.form["insta"],
    "noofsongs": request.form["noofsongs"],
    "noofplaylist": request.form["noofplaylist"],
    "country":request.form['country'],
    "start_date":request.form["start_date"],
    "end_date":request.form["end_date"]
    }

    print(data)
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
    formation = request.args.get("sort")
    if formation == "descending":
        return "LOL"
    else:

        # if conditions for formating based on the Amount value
        index =get_indexppt()
        file_loc = "maindata/potentialplaylists.json"
        data = {
            "id" : index+1 ,
            "Amount" : int(request.form["amount"]),
            "location" : request.form["location"],
            "playlist link" : getplaylistname(request.form["playlistlink"]),
            "Genre" : request.form["genre"],
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


# Seperate script for checking potential playlists.
var = "main"
@application.route("/potentialplaylists",methods= ["GET", "POST"])
def pplaylists():
    pptdata  = displayppt()
    countrynames = []
    for i in range(len(pptdata)):
        pptdata[i]["id"] = i+1
        pptdata[i]["Amount"] = f"${pptdata[i]['Amount']}"
        countrynames.append(pptdata[i]["location"])

    global countrylist
    countrylist = list(set(countrynames))
    print(countrylist)


    return render_template("potentialplaylists.html", pptdata = pptdata ,var=var,countrylist=list(set(countrylist)) )


# this function is for descending playlist.
var = "main"
@application.route("/potentialplaylists/descending",methods= ["GET", "POST"])
def descending():
    rcountrylist = []

    pptdata  = displayppt()[::-1]
    for i in range(len(pptdata)):
        pptdata[i]["id"] = i+1
        pptdata[i]["Amount"] = f"${pptdata[i]['Amount']}"
        rcountrylist.append(pptdata[i]['location'])
    fcountrylist = list(set(rcountrylist))

    return render_template("descending.html", pptdata = pptdata ,var=var, countrylist=list(set(fcountrylist)))



var="main"
@application.route("/<string:countryname>")
def getcountrylist(countryname):
    selectedCountry = countryname
    filterlist = []
    pptdata  = displayppt()
    countrynames = []
    # setting the counter for the filterlist
    # this take care of the index of the new filter list with random indexes.
    counter = 1
    for i in range(len(pptdata)):
        if pptdata[i]["location"]==countryname:
            pptdata[i]["id"] = counter
            pptdata[i]["Amount"] == f"${pptdata[i]['Amount']}"
            filterlist.append(pptdata[i])
            counter +=1
        else:
            pass


    countrylist.append("Location")
    # print(filterlist)
    # print(countrylist)
    return render_template("potentialplaylists.html", pptdata = filterlist ,var=var,countrylist=list(set(countrylist)) ,selectedCountry=selectedCountry)





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

@application.route("/alltime")
def alltimestats():
    return render_template("alltime.html" ,alltimeData = alltimeData)



# Work Here

# this the main functionality endpoint.(Adds data)
var = "main"
@application.route("/addplaylists")
def addplaylist():
    pldata = displaylists()
    return render_template("addplaylists.html", var=var,pldata=pldata)







var = "main"
ratepps = pps()
data = dict(ratepps)
@application.route("/ratepps")
def ratepps():
    return render_template("rate.html", data=data, var =var)







#################################### Endpoints below require more work ########################################
# miscellaneous
# about, main



@application.route("/login")
def login():
    return render_template("login.html")


# function to display error pages
@application.route("/<random>")
def error(random):
    return "Page not found!"

if __name__ == "__main__":
    application.run()
