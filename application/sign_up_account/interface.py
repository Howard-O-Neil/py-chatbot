import click
from application.sign_up_account.dto.sign_up_dto import SignUpDto
from application.share.utils import utils, print_all
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app, user_cli_group

from .service import service

@app.route(f"{ApiGroup.USER.value}/sign-up", methods=["POST"])
@secure.user_auth
@utils.validate(SignUpDto)
def sign_up(data):
    # print(data)
    return service.sign_up(data)


@user_cli_group.command('sign-up')
@click.option('-fb', 'facebook_url', help='Your user facebook url')
@click.option('-n', 'name', help='Your user name')
@click.option('-p', 'phone', help='Your phone number')
@click.option('-e', 'email', help='Your email address')
def sign_up(**kwargs):
    print(kwargs.get('facebook_url'))
    # service.sign_up(**kwargs)
    return 'hello world'