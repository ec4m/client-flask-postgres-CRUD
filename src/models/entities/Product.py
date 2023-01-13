class Product:
  def __init__(self, id, name=None, description=None, price=None):
    self.id = id
    self.name = name
    self.description = description
    self.price = price

  
  def to_JSON(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'price': self.price
    }