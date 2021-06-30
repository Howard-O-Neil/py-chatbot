from application.share.dialog_utils import dialogUtils
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import project_group, app
from .service import service
import click
import copy
import json

@project_group.command('add')
@click.option('-n', 'name', help='Project name')
@click.option('-t', 'slack_team_id', help='Project slack team/workspace id')
def sign_up(**kwargs):

    service.add_project(kwargs)
