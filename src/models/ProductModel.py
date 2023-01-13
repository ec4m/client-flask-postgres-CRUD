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
          products.append(product.to_JSON())
      conn.close()
      return products
      
    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def get_product(self, id):
    try:
      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, description, price FROM product WHERE id=%s", (id,))
        row = cursor.fetchone()
        product = None
        if row != None:
          product = Product(row[0], row[1], row[2], row[3])
          product = product.to_JSON()
        else:
          product = None
      conn.close()
      return product

    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def add_product(self, product):
    try:
      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("""INSERT INTO product (id, name, description, price)
                          VALUES (%s, %s, %s, %s)""", (product.id, product.name, product.description, product.price))
        affected_rows = cursor.rowcount
        conn.commit()
      conn.close()
      return affected_rows

    except Exception as ex:
      raise Exception(ex)

  
  @classmethod
  def delete_product(self, product):
    try:
      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("DELETE FROM product WHERE id=%s", (product.id,))
        affected_row = cursor.rowcount
        conn.commit()
      conn.close()
      return affected_row
        
    except Exception as ex:
      raise Exception(ex)
      

  @classmethod
  def update_product(self, product):
    try:
      conn = get_connection()
      with conn.cursor() as cursor:
        cursor.execute("UPDATE product SET name=%s, description=%s, price=%s WHERE id=%s", (product.name, product.description, product.price, product.id))
        affected_row = cursor.rowcount
        conn.commit()
      conn.close()
      return affected_row

    except Exception as ex:
      raise Exception(ex)