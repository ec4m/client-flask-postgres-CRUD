from flask import Blueprint, jsonify, request

import uuid

# Entities
from models.entities.Client import Client
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


@client.route('/add', methods=['POST'])
def add_client():
  try:
    id = uuid.uuid4()
    name = request.json['name']
    lastname = request.json['lastname']
    age = request.json['age']
    client = Client(str(id), name, lastname, age)

    affetered_rows = ClientModel.add_client(client)

    # validation
    if affetered_rows != None:
      return jsonify({'id': str(id)})
    else:
      return jsonify({'message': 'Error on insert.'}), 500

  except Exception as ex:
    return jsonify({'message': str(ex)}), 500


@client.route('/delete/<id>', methods=['DELETE'])
def delete_client(id):
  try:
    client = Client(id)
    affected_row = ClientModel.delete_client(client)
    if affected_row != None:
      return jsonify(client.id)
    else:
      return jsonify({'message': 'No client deleted.'})

  except Exception as ex:
    return jsonify({'message': str(ex)})