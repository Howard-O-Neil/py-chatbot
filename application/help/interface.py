from application.share.dialog_utils import dialogUtils
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import project_group, db
import click
import copy
import json

@app.route(f"{ApiGroup.USER.value}/help", methods=["POST"])
@utils.request_with_body
def user_help(data):
    current_intent = data["currentIntent"]

    response_content = ""
    for item in [
        "show some available meeting duration",
        "i want a meeting",
        "show some available task",
        "my current task",
        "mark done task",
        "i want logwork",
    ]:
        response_content += f'\n>{item}'

    result = dialogUtils.close("Fulfilled")
    result["dialogAction"]["message"] = {
        "contentType": "PlainText",
        "content": f"Here are some recommend command:\
                    \
                    {response_content}",
    }

    return result