from flask import Flask,abort
from data import me,mock_catalog


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

#get/api/catalog
# return the list of products as JSON
@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)

#get/api/count
# return the number of products on the list
@app.get("/api/catalog/count")
def count_products():
    count = len(mock_catalog)
    return json.dumps(count)

@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results=[]
    for prod in mock_catalog:
        if prod["category"]==cat:
            results.append(prod)
            
    return json.dumps(results)
            
# create an endpoint that allows to retrieve a product by its _id
# the endpoint should be a get on /api/product/5 where is an _id

@app.get("/api/product/<id>")
def prod_by_id(id):
    #find the product with _id equal to id
    # return it as jsom string
    for prod in mock_catalog:
        if prod["_id"] ==id:
            return json.dumps(prod)
    
    #not found
    return abort(404, "Invalid id")

# get/api/product/search/xyz
# search products whose title CONTAINS xyz

@app.get("/api/product/search/<text>")
def prod_search(text):
    results=[]
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod) 
    return json.dumps(results)

 

@app.get("/api/categories")
def get_categories():
    results=[]
    for prod in mock_catalog:
        cat = prod["category"]
        if not cat in results:
            results.append(cat)
            
    return json.dumps(results)

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