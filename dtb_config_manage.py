from entities.configuration import Configuration
import click
from app import db, app

def update_row(config):
    db.session.commit()

def add_row(config):
    db.session.add(config)
    db.session.commit()

class DB_Config(object):
    def get(self, key):
        res = db.session.query(Configuration).filter(Configuration.key==key).first()

        if res == None:
            raise KeyError(f'Not found key with name {key}')
        return res.value


@app.cli.command("db-config")
@click.option('--add/--update', default=True, help="add: add new record to database\
                                                    update: update existed record in database")
@click.option('-k', 'key')
@click.option('-v' ,'value')
def db_config_command(**kwargs):

    config = Configuration(
        key=kwargs.get('key'),
        value=kwargs.get('value')
    )
    if kwargs.get('add'):
        add_row(config)
    if kwargs.get('update'):
        update_row(config)
