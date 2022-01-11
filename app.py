import flask
from flask import *
import json
# from flask import Flask,escape
# from flask import render_template
# from flask import send_file
from collections import OrderedDict
from rate import pps
from helpfunc import displaylists, get_index,displayppt
from helpfunc import get_indexppt,getplaylistname,blacklistus
import os

app = Flask(__name__)


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
@app.route("/main")
def main():
    return render_template("index.html" , jData=jData, var=ab)

###############################################GOD Function ########################################################
# handling the add playlist submission data
@app.route('/handle_data', methods=['POST'])
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
@app.route("/handle_ppt", methods=['POST'])
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

@app.route("/handle_blacklist", methods=["POST"])
def handle_blacklist():
    link = request.form["blacklist"]
    # if link.startswith("https://open.spotify.com/user/"):
    data = blacklistus(link)


#############################seven days endpoint #################################
@app.route("/sevendays")
def seven_days():
    return render_template("sevendays.html" ,sdData =sdData)

##############################24 hours end point######################################
@app.route("/24hours")
def tf_hours():
    return render_template("tfhours.html" ,tfData =tfData)

# Work Here

# this the main functionality endpoint.(Adds data)
var = "main"
@app.route("/addplaylists")
def addplaylist():
    pldata = displaylists()
    return render_template("addplaylists.html", var=var,pldata=pldata)


# Seperate script for checking potential playlists.
@app.route("/potentialplaylists")
def pplaylists():
    pptdata  = displayppt()
    return render_template("potentialplaylists.html", pptdata = pptdata)



ratepps = pps()
data = dict(ratepps)
@app.route("/ratepps")
def ratepps():
    return render_template("rate.html", data=data)




#################################### Endpoints below require more work ########################################



# miscellaneous
# about, main
var = "main"
@app.route("/tutorial")
def tut():
    return render_template("tutorial.html", var=var)

var = "main"
@app.route("/blacklist")
def blacklist():
    return render_template("blacklist.html", var=var)

# function to display error pages
@app.route("/<random>")
def error(random):
    return "page not found, Bad Request"

app.run("127.0.0.1",port=8080 debug=True)