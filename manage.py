# this file is a cli command management

from flask_script.commands import Command
from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

print(Config.SQLALCHEMY_DATABASE_URI)

app.config.from_object(Config)
migrate = Migrate(app, db)
manager = Manager(app)

@manager.option('-n', '--name', dest='name')
def hello(name):
  print("hello", name)

manager.add_command('db', MigrateCommand)

if (__name__ == '__main__'):
  manager.run()