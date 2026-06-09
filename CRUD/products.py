 # imported packages required to create REST APIs with Flask
from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {"id": 143, "name": "Notebook", "price": 5.49},
    {"id": 144, "name": "Black Marker", "price": 1.99},
]

#
# Add all the REST API end-points here

# retrieve all the products with GET request
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# retrieve a product by its id
@app.route('/products/<id>', methods=['GET'])
def get_product():
    id = int(id)
    products = [x for x in products if x["id"] == id][0]
    return jsonify(products)

# add a product with POST req method
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return 'product added', 201

# update a product by its id with PUT req method
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    update_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in update_product.items():
         product[key] = value

    return 'product updated',  204

# delete product by its id with DELETE method
@app.route('/product', methods=['DELETE'])
def remove_product():
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    
    return 'product removed', 204



app.run(port=5000, debug=True)
