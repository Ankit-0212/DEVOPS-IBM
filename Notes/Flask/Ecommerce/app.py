from flask import Flask,jsonify
from servicelayer import loadProducts,write_products


app = Flask(__name__)

products = loadProducts()

@app.get("/api/products")
def load_products():
    return jsonify({'products':products})

@app.get("/api/products/<string:productName>")

def getProducts(productName):
    for product in products:
        if product['productName'] == productName:
            content = {
                "Product Name": product['productName'],
                "Brand ": product['brand'],
                "Price ": product['price']
            }
            return jsonify([{"ProductDetails": content}])

    return jsonify([{"Error": "Noo Products Found"}]) , 404


@app.patch("/api/order/<string:productName>/<int:quantity>")
def orderProduct(productName,quantity):
    print(products)
    for product in products:
        if product['productName'] == productName and quantity <= int(product['quantity']):
            product['quantity'] = str(int(product['quantity']) - quantity)
            content = {
                "productName": product['productName'],
                "Brand": product['brand'],
                "quantity": quantity,
                "totalPrice": quantity * int(product['price']),
                "status": "Order Placed"
            }
            write_products(products)
            return jsonify([{"OrderDetails": content}]), 200
        else:
            content = {
                "Error": "Quantity Not Satisfied",
                "status": "Order Not Placed"
            }
            return jsonify([{"OrderDetails": content}]), 404
    return jsonify([{"Error": "No Products Found"}]), 404








