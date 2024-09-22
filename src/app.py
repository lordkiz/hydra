#!flask/bin/python
from flask import Flask
from v1.routes import bp as v1_blueprint

app = Flask(__name__)

app.register_blueprint(v1_blueprint, url_prefix='/v1')

if __name__ == '__main__':
  app.run(debug=True)
  