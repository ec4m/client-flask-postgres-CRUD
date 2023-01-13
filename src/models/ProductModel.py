from database.db import get_connection
from .entities.Product import Product

class ProductModel:
  @classmethod
  def get_products(self):
    try:
      conn = get_connection()
      products = []
      with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, description, price FROM product ORDER BY name ASC")
        resultset = cursor.fetchall()
        for row in resultset:
          product = Product(row[0], row[1], row[2], row[3])
          products.append(product)
      conn.close()
      return products
      
    except Exception as ex:
      raise Exception(ex)