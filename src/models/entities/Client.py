class Client:

  def __init__(self, id, name=None, lastname=None, age=None) -> None:
    self.id = id
    self.name = name
    self.lastname = lastname
    self.age = age

  def to_JSON(self):
    return {
      'id': self.id,
      'name': self.name,
      'lastname': self.lastname,
      'age': self.age
    }
    