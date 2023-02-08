from flask import Flask
from data import me

import json

app = Flask(__name__) #create a new instance, similar to new Task in JS

@app.get("/")
def home():
    return "Hello World!"

@app.get("/about")
def about():
    return "Kevin Fierro"

@app.get("/contact/me")
def contact_me():
    return "kfierro@uabc.edu.mx"

##########################################################
###################### API -> JSON #######################
##########################################################

@app.get("/api/developer")
def developer():
    return json.dumps(me) #parse me into a json

@app.get("/api/developer/adress")
def dev_adress():
    address= me["address"]
    # return address["street"] + " #" +address["city"] +", " + address["zipcode"]
    #f string
    return f'{address["street"]}, #{address["city"]}, {address["zipcode"]}'

app.run(debug=True)