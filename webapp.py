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
@app.route("/main")
def main():
    return render_template("index.html" , jData=jData)



@app.route("/sevendays")
def seven_days():
    return render_template("sevendays.html")


# potential pages


app.run("127.0.0.1",port=8080 ,debug=True)
