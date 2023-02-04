import json
from flask import Flask, render_template, url_for, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



@app.route("/") 
def default(): 
    return redirect(url_for("translate"))
 
@app.route("/translate/") 
def translate(): 
    return render_template("setting.html")


  

if __name__ == "__main__":
    app.run(debug=True)
