import flask
import json
from flask import Flask,escape
from flask import render_template
from flask import send_file

app = Flask(__name__)

file = open("dump.json", "r")
a = json.load(file)
print(a)
@app.route("/")
def hello_world():
    # return send_file("templates/index.html")






@app.route("/main")
def main():
    return "very good"



app.run("127.0.0.1",port=8080 ,debug=True)
