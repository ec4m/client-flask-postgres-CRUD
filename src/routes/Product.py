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
