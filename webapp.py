from flask import Flask, request, Markup, render_template, flash
import os
import json


app = Flask(__name__)

@app.route("/")
def render_main():
     return render_template('index.html')

@app.route("/Page1")
def render_main():
     return render_template('Page1.html')

@app.route("/Page2")
def render_main():
     return render_template('Page2.html')


if __name__ == "__main__":
    app.run(debug=True)
