from flask import Blueprint, jsonify

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