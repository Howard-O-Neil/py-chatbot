from application.share.dialog_utils import dialogUtils
import click
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app
from .service import service
import copy
import json


@app.route(f"{ApiGroup.PROJECT.value}/validate/is-signed", methods=["GET"])
@utils.request_with_param
def check_is_signed_project(admin_id, team_id):
    
    return service.check_is_signed_project(admin_id, team_id)