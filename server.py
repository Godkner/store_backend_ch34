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

 

# @app.get("/api/categories")
# def get_categories():
#     results=[]
#     for prod in mock_catalog:
#         cat = prod["category"]
#         if cat==category:
#             results.append(prod["category"])
    
#     res= set(results)
#     return json.dumps(res)
            
            
        
            
    
app.run(debug=True)