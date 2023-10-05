from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="my_db"
)

cursor = db.cursor()


@app.route('/registeruser', methods=['POST'])
def register_user():

    data = request.jsongit commit -m "first commit"
    username = data['username']


    return jsonify({"message": "User registered successfully"})


@app.route('/getallproducts', methods=['GET'])
def get_all_products():


    return jsonify({"products": products})

@app.route('/order', methods=['POST'])
def create_order():

    data = request.json


    return jsonify({"message": "Order created successfully"})

# Endpoint 4: Get all orders
@app.route('/allorders', methods=['GET'])
def get_all_orders():


    return jsonify({"orders": orders})


@app.route('/addproduct', methods=['POST'])
def add_product():

    data = request.json


    return jsonify({"message": "Product added successfully"})


@app.route('/updateproduct/<int:product_id>', methods=['PUT'])
def update_product(product_id):

    data = request.json


    return jsonify({"message": "Product updated successfully"})


@app.route('/deleteproduct/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):


    return jsonify({"message": "Product deleted successfully"})

@app.route('/getuser/<int:user_id>', methods=['GET'])
def get_user(user_id):


    return jsonify({"user": user})


@app.route('/getallusers', methods=['GET'])
def get_all_users():



    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)