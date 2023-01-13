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
          users.append(user.to_JSON())

      conn.close()
      return users

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def get_user(self,id):
    try:
      conn = get_connection()

      with conn.cursor() as cursor:
        cursor.execute("SELECT id, username, name, lastname, password FROM usuario WHERE id = %s", id)
        row = cursor.fetchone()

        user = None
        if row != None:
          user = User(row[0], row[1], row[2], row[3], row[4])
          user = user.to_JSON()

      conn.close()
      return user

    except Exception as ex:
      raise Exception(ex)

    
  @classmethod
  def add_user(self, user):
    try:
      conn = get_connection()

      with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO usuario (id, username, name, lastname, password) 
                          VALUES (%s, %s, %s, %s, %s)""", (user.id, user.username, user.name, user.lastname, user.password))
        affected_row = cursor.rowcount
        conn.commit()
      
      conn.close()
      return affected_row

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def delete_user(self, user):
    try:
      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (user.id,))
        affected_row = cursor.rowcount
        conn.commit()

      conn.close()
      return affected_row

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def update_user(self, user):
    try:
      conn = get_connection()
      
      with conn.cursor() as cursor:
        cursor.execute("UPDATE usuario SET username=%s, name=%s, lastname=%s, password=%s WHERE id=%s", (user.username, user.name, user.lastname, user.password, user.id))
        affected_row = cursor.rowcount
        conn.commit()

      conn.close()
      return affected_row
      
    except Exception as ex:
      raise Exception(ex)