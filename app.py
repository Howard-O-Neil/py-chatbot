import os
import click
from flask.cli import AppGroup
from flask_migrate import Migrate
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from faker.providers import lorem, company
from botocore.config import Config as AWS_CONFIG
import boto3
import threading

lex_client = boto3.client('lex-runtime')

fake = Faker('en_US')
fake.add_provider(lorem)
fake.add_provider(company)


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


db.init_app(app)
migrate.init_app(app, db)


# group command

@click.group('project')
def project_group():
    pass

@click.group('user')
def user_group():
    pass

@click.group('noti')
def notification_group():
    pass

# add group
app.cli.add_command(project_group)
app.cli.add_command(user_group)
app.cli.add_command(notification_group)

__import__("entities")
__import__("application")
__import__("dtb_config_manage")

@app.route("/")
def index():
    return "py-chatbot version 1.0"

if __name__ == "__main__":
    if Config.FLASK_ENV != "production":
        app.run(debug=True)
        threading.Thread(target=app.run).start()
    else:
        app.run(debug=False)
        threading.Thread(target=app.run).start()