from flask import Flask , render_template, request ,redirect,url_for
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from os import error

app = Flask(__name__,template_folder="template")


load_dotenv("flaskr\.env")
url= os.environ["MONGODB_URI"]
client = MongoClient(url)

db = client.Desafio
loginCollection= db.login
cadastroCollection = db.cadastro
collectionEmpresas = db.Empresas
collectionSocios = db.Sócios
collectionsEstabelecimentos = db.Estabelecimentos

error = None


@app.route("/",methods=["GET","POST"])
def register():
    
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"]
       error =  None
       
       if not username:
           error = "É preciso do Username"
       elif not password:
           error  = "É preciso da Password" 
       
       if error is None:
           try:
               cadastroCollection.insert_one({"Username":username,"Password":password})
           except cadastroCollection.find({"Username":username,"Password":password}):
               error=f"Usuário {username} já cadastrado"  
               loginCollection.insert_one({"Username":username,"Password":password}) 
               
    return redirect('/data') 
    #    if loginCollection.find({username,password}) == False:
    #        print("Você ainda não está cadastrado")
    #        cadastroCollection.insert_one({"username":username,"password":password})
    #    else:
    #        loginCollection.insert_one({"username":username,"password":password})
    
    

 
@app.route('/data',methods=["GET","POST"])
def datalist():  
    if request.method == "GET":
        return redirect('/filter')
    
    if request.method == "POST":
         return render_template("datalist.html")



@app.route('/filter',methods=["GET","POST"])
def filter():
    if request.method == "GET":
         cnpjem =  request.form["cnpjem"]
         rses = request.form["rses"]
         lso  = request.form["lso"]
         if cnpjem and rses and lso == True:
          a =  collectionEmpresas.find_one({cnpjem})
          b =  collectionEmpresas.find_one({rses})
          c =  collectionsEstabelecimentos.find_one({lso})
          if a and b and c == True:
                   return "<p>Os dados são verdadeiros</p>"
          else:     
                    return "<p>Os dados não são verdadeiros</p>"
    
    
    if request.method == "POST": 
         return render_template('filter.html',cnpjem=cnpjem,rses=rses,lso=lso)            
    
