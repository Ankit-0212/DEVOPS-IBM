from flask import Flask,jsonify,request
from datetime import datetime
from loadproducts import laod_products,write_products
import json
app = Flask(__name__)
products = laod_products()





@app.get("/api/products")
# @app.route(rule="/api/products",methods=["GET"])
def load_products():
    return jsonify({'products':products})


@app.get("/api/products/<string:productName>")
@app.route(rule="/api/products",methods=["GET"])
def get_products_by_name(productName):
    filteredproducts = list(filter(lambda product:product['productName'] == productName,products))
    if len(filteredproducts) != 0:
        return jsonify( filteredproducts )
    else:
        return jsonify({ "productName": "ProductName Not Found" }), 404


@app.delete("/api/products/<int:productId>")
def delete_product_by_id(productId):
    if len(products)==0:
        return jsonify({'products': 'Product is empty nothing to delete'})
    
    for product in products:
        if product['productId']==productId:
            products.remove(product)
            write_products(products)
            return jsonify({'products': 'Product is removed'})
    return jsonify({'products': 'No products found to delete'})
    
    
@app.post("/api/products")
def add_new_product():
    request_data = request.get_json()
    # print(request_data)
    products.append(request_data)
    write_products(products)
    return jsonify({'products':"Products Added"})


