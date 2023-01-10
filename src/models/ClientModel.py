from database.db import get_connection
from .entities.Client import Client



class ClientModel:

  @classmethod
  def get_clients(self):
    try:
      conn = get_connection()
      clients = []

      with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, lastname, age FROM client ORDER BY id ASC ")
        resultset = cursor.fetchall()

        for row in resultset:
          client = Client(row[0], row[1], row[2], row[3])
          clients.append(client.to_JSON())

      conn.close()
      return clients

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def get_client(self,id):
    try:
      conn = get_connection()

      with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, lastname, age FROM client WHERE id = %s", id)
        row = cursor.fetchone()

        client = None
        if row != None:
          client = Client(row[0], row[1], row[2], row[3])
          client = client.to_JSON()

      conn.close()
      return client

    except Exception as ex:
      raise Exception(ex)