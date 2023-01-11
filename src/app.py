from flask import Flask

# config
from config import config

# Routes
from routes import Client, User

app = Flask(__name__)

def page_not_found(error):
  return "<h1>Page no found - Página no encontrada</h1>"

if __name__ == '__main__':
  app.config.from_object(config['development'])

  app.register_blueprint(Client.client, url_prefix='/api/client')
  app.register_blueprint(User.user, url_prefix='/api/user')

  app.register_error_handler(404, page_not_found)
  app.run(debug=True, port=3000)