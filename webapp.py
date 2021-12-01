import flask
from flask import *
import json
from flask import Flask,escape
from flask import render_template
from flask import send_file
from collections import OrderedDict
import os
app = Flask(__name__)

file = open("tedays.json", "r", encoding="utf-8")
jData = json.load(file)

# sd is sevenday file
sdfile = open("sevendays.json", "r", encoding="utf-8")
sdData = json.load(sdfile)
# print(jData)

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
    data = {
    "id" : request.form["id"],
    "amount_paid":request.form["amount_paid"],
    "playlistlink":request.form["playlistlink"],
    "country":request.form['country'],
    "start_date":request.form["start_date"],
    "end_date":request.form["end_date"]
    }

    with open("addplaylist.json" , "r+") as file:

        # working on presistent data in add playlist.json
        # mydict = OrderedDict()
        # ls = []
        # jsonsize = os.path.getsize("addplaylist.json")
        # if jsonsize ==0:
        #     ls.append(data)
        #     mydict["PlayList Data"] = ls
        #     json.dump(mydict,file)
        #     return "Entry one added"
        # elif jsonsize!=0:
        #     per = OrderedDict()
        #
        #     aldata = json.load(file)
        #     dic = data
        #     aldata['PlayList Data'].append(dic)
        #     per = aldata
        #
        #     # file.truncate(0)
        #     json.dump(per,file)
        #     return "another entry added"



#############################################################################
@app.route("/sevendays")
def seven_days():
    return render_template("sevendays.html" ,sdData =sdData)


# Seperate script for checking potential playlists.
@app.route("/potentialplaylists")
def pplaylists():
    return render_template("potentialplaylists.html")


var = "main"
@app.route("/addplaylists")
def addplaylist():
    return render_template("addplaylists.html", var=var)



# miscellaneous
# about, main
var = "main"
@app.route("/tutorial")
def tut():
    return render_template("tutorial.html", var=var)




# function to display error pages
@app.route("/<name>")
def error(name):
    return "error"

app.run("127.0.0.1",port=8080 ,debug=True)
