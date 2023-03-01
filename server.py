from flask import Flask,abort,request
from data import me,mock_catalog
from config import db
from bson import ObjectId

import json



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

@app.get("/api/developer/address")
def dev_address():
    address= me["address"]
    # return address["street"] + " #" +address["city"] +", " + address["zipcode"]
    #f string
    return f'{address["street"]}, #{address["city"]}, {address["zipcode"]}'

def fix_id(obj):
    obj["_id"] = str(obj["_id"])

#get/api/catalog
# return the list of products as JSON
@app.get("/api/catalog")
def get_catalog():
    cursor= db.products.find({})
    results= []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
    return json.dumps(results)

@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)
    
    print("-" * 25)
    print(data)
    fix_id(data)
    return json.dumps(data)

#get/api/count
# return the number of products on the list
@app.get("/api/catalog/count")
def count_products():
    total= db.products.count_documents({})
    return json.dumps(total)
#python pymongo  count docs on a collection

@app.get("/api/category/<cat>")
def prods_by_category(cat):
    cursor = db.products.find({"category":cat})#filter on db
    results=[]
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
            
    return json.dumps(results)
            
# create an endpoint that allows to retrieve a product by its _id
# the endpoint should be a get on /api/product/5 where is an _id

@app.get("/api/product/<id>")
def prod_by_id(id):
    _id = ObjectId(id)
    prod = db.products.find_one({"_id": _id})
    if prod is None:
        return abort(404, "Invalid id")
    fix_id(prod)
    return json.dumps(prod)
    # #find the product with _id equal to id
    # # return it as json string
    # for prod in mock_catalog:
    #     if prod["_id"] ==id:
    #         return json.dumps(prod)
    
    #not found
   

# get/api/product/search/xyz
# search products whose title CONTAINS xyz

@app.get("/api/product/search/<text>")
def prod_search(text):
    cursor =db.products.find({"title": {"$regex": text, "$options": "i"} })
    results= []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
    return json.dumps(results)
    # results=[]
    # for prod in mock_catalog:
    #     if text.lower() in prod["title"].lower():
    #         results.append(prod) 
    # return json.dumps(results)

 

@app.get("/api/categories")
def get_categories():
    cursor =db.products.distinct("category")
    return json.dumps(list(cursor))
    # results=[]
    # for prod in mock_catalog:
    #     cat = prod["category"]
    #     if not cat in results:
    #         results.append(cat)
            
        # return json.dumps(results)

#should return the sum of all prices
@app.get("/api/total")
def get_total():
    total=0
    for prod in mock_catalog:
        total += prod["price"]
        
    return json.dumps(total)
    

#return all the products (list) width price lower or equal to <price>
# note price will be an string
@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    results= []
    for prod in mock_catalog:
        if prod["price"]<=float(price):
            results.append(prod)
    
    return json.dumps(results)
            
# challenge
# find and return the cheapest product

# create a cheapest = mock_catalog[0]
# for loop to travel the list
# get every prod from the list
# if the price of prod is lower than the price of cheapest
# then update cheapest to be the prod (cheapest = prod)
@app.get("/api/cheapest")
def get_cheapest():
    result = mock_catalog[0]
    for prod in mock_catalog:
        if prod["price"] < result["price"]:
            result = prod

    return json.dumps(result)
            
            
        
            
    
app.run(debug=True)