from flask import Flask, request, Markup, render_template, flash
import os
import json


app = Flask(__name__)

@app.route("/")
def render_main():
     return render_template('index.html')

@app.route("/Page1")
def render_one():
     return render_template('Page1.html', state_options = state_options())

def state_options():
    ListofStates = []
    options = ""
    with open('finance(1).json') as finance:
        states = json.load(finance)
    for State in states:
        S = State["State"]
        if not S in ListofStates:
            ListofStates.append(S)
    for State in states:
        options += Markup("<option value=\"" +S+ "\">" +S+ "</option>")
    return options

@app.route("/Page2")
def render_two():
     return render_template('Page2.html')


if __name__ == "__main__":
    app.run(debug=True)
