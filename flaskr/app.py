
from flask import Flask , render_template, request ,url_for
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__,template_folder="template")

load_dotenv("flaskr\.env")
url= os.environ["MONGODB_URI"]
client = MongoClient(url)

db = client.Desafio
loginCollection= db.login
cadastroCollection = db.cadastro


class User:

    def verifyuser(self):
            username = request.form.get("username")
            password = request.form.get("password")
            loginCollection.insert_many({username,password})
            if loginCollection.find({username,password}) == False:
                cadastroCollection.insert_one({username,password})
        


@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
       return User.verifyuser()
    
    return render_template("index.html")

    








