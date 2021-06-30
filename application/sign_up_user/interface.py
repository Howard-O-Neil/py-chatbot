from application.share.api_constraint import ApiGroup
import click
from application.share.utils import stdout, utils, print_all
from application.share.security import secure
from app import user_group, app

from .service import service

@app.route(f"{ApiGroup.USER.value}/list/sign-up", methods=["POST"])
@utils.request_with_body
def sign_up_multiple_user(data):
    stdout(data)
    pass

@user_group.command('add')
@click.option('-n', 'name', help='Your user real name')
@click.option('-p', 'phone', help='Your user phone')
@click.option('-e', 'email', help='Your user email')
@click.option('-t', 'team_id', help='Your user team id')
@click.option('-u', 'user_id', help='Your user id')
def sign_up(**kwargs):
    return service.sign_up(kwargs)