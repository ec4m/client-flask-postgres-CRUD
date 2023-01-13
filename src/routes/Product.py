from flask import Blueprint, jsonify, request

import uuid

# Entites
from models.entities.Product import Product
# Models
from models.ProductModel import ProductModel

product = Blueprint('product_blueprint', __name__)

@product.route('/')
def get_products():
  try:
    products = ProductModel.get_products()
    return jsonify(products)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/<id>')
def get_product(id):
  try:
    product = ProductModel.get_product(id)
    if product != None:
      return jsonify(product)
    else:
      return jsonify({'message': 'Product not found'})
    
  except Exception as ex:
    return jsonify({'message': str(ex)})


@product.route('/add', methods=['POST'])
def add_product():
  try:
    id = uuid.uuid4()
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    product = Product(str(id), name, description, price)
    affected_row = ProductModel.add_product(product)

    if affected_row != None:
      return jsonify(product.id)
    else: 
      return jsonify({'message': 'Error on insert'})

    
  except Exception as ex:
    return jsonify({'message': str(ex)})