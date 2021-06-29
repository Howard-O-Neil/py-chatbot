from application.share.dialog_utils import DialogUtils, dialogUtils
from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from entities.user import User
from .repository import repository

import json

class Service:
    @utils.handle_service_error
    def check_is_signed_project(self, admin_id, team_id):
        res = repository.find_by_admin_team(admin_id, team_id)
        if len(res) == 0:
            return json.dumps({
                "status": "failed",
                "message": "your team/workspace is not signed up yet"
            })
        return json.dumps({
            "status": "ok",
            "message": ""
        })
        

service = Service()