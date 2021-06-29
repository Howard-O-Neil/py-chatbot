import click
from application.share.utils import utils, print_all
from application.share.security import secure
from app import user_group

from .service import service


@user_group.command('add')
@click.option('-n', 'name', help='Your user real name')
@click.option('-p', 'phone', help='Your user phone')
@click.option('-e', 'email', help='Your user email')
@click.option('-t', 'team_id', help='Your user team id')
@click.option('-s', 'slack_id', help='Your user slack id')
def sign_up(**kwargs):
    return service.sign_up(kwargs)