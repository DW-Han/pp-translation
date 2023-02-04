import json
from flask import Flask, render_template, url_for, request, redirect, session, jsonify

app = Flask(__name__)



@app.route("/") 
def default(): 
    return render_template("setting.html")
 
@app.route("/translate/") 
def translate(): 
    return render_template("setting.html")


  

if __name__ == "__main__":
    app.run(debug=True)
