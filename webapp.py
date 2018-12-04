from flask import Flask, request, Markup, render_template, flash
import os
import json


app = Flask(__name__)

@app.route("/")
def render_main():
     return render_template('index.html')

@app.route("/Page1")
def render_one():
    try :
        year = request.args["Year"]
        state = request.args["State"]
        data = spfc_finance(year, state)
        return render_template('Page1.html', state_options = state_options(), data = data)
    except:
        return render_template('Page1.html', state_options = state_options(), data = {"exist":'no'})



def state_options():
    ListofStates = []
    options = ""
    with open('finance(1).json') as finance:
        states = json.load(finance)
    for State in states:
        S = State["State"]
        if not S in ListofStates:
            ListofStates.append(S)
    for State in ListofStates:
        options += Markup("<option value=\"" +State+ "\">" +State+ "</option>")
    return options

@app.route("/Page2")
def render_two():
     return render_template('Page2.html')

def spfc_finance(year, state):
    with open ('finance(1).json') as finance:
        specific = json.load(finance)
    for data in specific:
        if data["Year"] == year and data["State"] == state:
            return data



if __name__ == "__main__":
    app.run(debug=True)
