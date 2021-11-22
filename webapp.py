import flask
import json
from flask import Flask,escape
from flask import render_template
from flask import send_file

app = Flask(__name__)

file = open("dump.json", "r", encoding="utf-8")
jData = json.load(file)
# print(jData)

# Home Route
ab = "tutorial"
@app.route("/main")
def main():
    return render_template("index.html" , jData=jData, var=ab)




@app.route("/sevendays")
def seven_days():
    return render_template("sevendays.html")


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
