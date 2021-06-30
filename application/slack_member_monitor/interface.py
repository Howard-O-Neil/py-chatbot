from application.share.dialog_utils import DialogUtils, dialogUtils
import click
from application.share.utils import stdout, utils, print_all
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app

from .service import service

@app.route(f"{ApiGroup.SLACK_MEMBER.value}/member/event", methods=["POST"])
@utils.request_with_body
def slack_member_monitor(data):
    event_type = data["body"]["event"]["type"]
    stdout(data)
    if event_type == "user_change":
        return service.user_change_handle(data["body"])
    elif event_type == "team_join":
        return service.user_join_handle(data["body"])
    
    return {
        "status": "ok",
        "message": "undefined event type"
    }
