class User:


  def __init__(self, id, username=None, name=None, lastname=None, password=None):
    self.id = id
    self.username = username
    self.name = name
    self.lastname = lastname
    self.password = password


  def to_JSON(self):
    return {
      'id': self.id,
      'username': self.username,
      'name': self.name,
      'lastname': self.lastname,
      'password': self.password
    }