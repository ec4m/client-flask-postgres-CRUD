from database.db import get_connection
from .entities.User import User



class UserModel:

  @classmethod
  def get_users(self):
    try:
      conn = get_connection()
      users = []

      with conn.cursor() as cursor:
        cursor.execute("SELECT id, username, name, lastname, password FROM usuario ORDER BY id ASC ")
        resultset = cursor.fetchall()

        for row in resultset:
          user = User(row[0], row[1], row[2], row[3], row[4])
          print(user.to_JSON())
          users.append(user.to_JSON())

      conn.close()
      return users

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def get_user(id):
    conn = get_connection()

    with conn.cursor() as cursor:
      cursor.execute("SELECT id, username, name, lastname, password FROM usuario WHERE id = %s", id)
      row = cursor.fetchone()

      user = None
      if row != None:
        user = User(row[0], row[0], row[0], row[0], row[0], )