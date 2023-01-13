from flask import Blueprint, jsonify, request

import uuid

# Entities
from models.entities.User import User
# Models
from models.UserModel import UserModel


user = Blueprint('user_blueprint', __name__)


@user.route('/')
def get_users():
  try:
    users = UserModel.get_users()
    return jsonify(users)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@user.route('/<id>')
def get_user(id):
  try:
    user = UserModel.get_user(id)
    if user != None:
      return jsonify(user)
    else:
      return jsonify({})
  except Exception as ex:
    return jsonify({'message': str(ex)})

  
@user.route('/add', methods=['POST'])
def add_user():
  try:
    id = uuid.uuid4()
    username = request.json['username']
    name = request.json['name']
    lastname = request.json['lastname']
    password = request.json['password']

    user = User(str(id), username, name, lastname, password)

    affected_row = UserModel.add_user(user)

    return jsonify(affected_row)
  except Exception as ex:
    return jsonify({'message': str(ex)})


@user.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User(id)
    affected_row = UserModel.delete_user(user)

    if affected_row != None:
      return jsonify(user.id)
    else:
      return jsonify({'message': 'No deleted user'})

  except Exception as ex:
    return jsonify({'message': str(ex)})