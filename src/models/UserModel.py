from database.db import get_connection

class UserModel:

  @classmethod
  def get_user(self):
    conn = get_connection()
    users = []

    with conn.cursor() as cursor:
      pass