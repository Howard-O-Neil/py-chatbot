import os
import click
from flask.cli import AppGroup
from flask_migrate import Migrate
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)
migrate.init_app(app, db)

from models import *

@app.route('/')
def index():
  return "py-chatbot version 1.0"

# group command
@click.group()
def test(): pass

@test.command()
@click.argument('name')
def hello(name):
  print(os.environ.get('POSTGRES_HOST'))
  print("hello", name)

# add group
app.cli.add_command(test)

if __name__ == '__main__':
  if Config.FLASK_ENV != 'production': app.run(debug=True)
  else: app.run(debug=False)  