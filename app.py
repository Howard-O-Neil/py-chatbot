from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
  return "py-chatbot version 1.0"

if __name__ == '__main__':
  if Config.FLASK_ENV != 'production': app.run(debug=True)
  else: app.run(debug=False)  