from dotenv import load_dotenv
import os

def loadEnv():
  environPath = None

  flask_env = os.environ.get('FLASK_ENV')
  environPath = f"{'development' if flask_env is None else flask_env}.env"

  load_dotenv(environPath)

loadEnv()

class Config(object):
  # DB_HOST = os.environ.get('POSTGRES_HOST'),
  # DB_USER = os.environ.get('POSTGRES_USER'),
  # DB_PASS = os.environ.get('POSTGRES_PASSWORD'),
  # DB_NAME = os.environ.get('POSTGRES_DB'),

  # app config 
  SECRET_KEY = os.environ.get('SECRET_KEY'),
  FLASK_ENV = os.environ.get('FLASK_ENV'),
  FLASK_APP = os.environ.get('FLASK_APP')


  SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')},{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"
  SQLALCHEMY_ECHO = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False