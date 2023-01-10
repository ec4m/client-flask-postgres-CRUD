from flask import Blueprint, jsonify

# Entities
# from models.entities.Client import Client
# Models
from models.ClientModel import ClientModel

client = Blueprint('client_blueprint', __name__)

@client.route('/')
def get_clients():
  try:
    clients = ClientModel.get_clients()
    return jsonify(clients)
  except Exception as ex:
    return jsonify({'message': str(ex)}), 500

@client.route('/<id>')
def get_client(id):
  try:
    client = ClientModel.get_client(id)
    if client != None:
      return jsonify(client)
    else:
      return jsonify({})
  except Exception as ex:
    return jsonify({'message': str(ex)}), 500