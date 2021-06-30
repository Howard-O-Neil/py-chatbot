from functools import reduce

from dateutil import parser
from application.share.dialog_utils import dialogUtils
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app, user_group
from .service import service
import click
import re


def check_full_slots(list_slot, slots):
    for name in list_slot:
        if slots[name] == None:
            return False
    return True


@app.route(f"{ApiGroup.USER.value}/task/available", methods=["POST"])
@utils.request_with_body
def available_task(data):
    user_id = data["userId"]
    current_intent = data["currentIntent"]

    response_content = ""
    for item in service.get_available_task(user_id.split(":")[1], 5):
        response_content += f'\n\n>*Task*:          {item["id"]}\
                                   >name:           {item["name"]}\
                                   >status:         {item["status"]}\
                                   >estimated:      {item["estimate"]}'

    result = dialogUtils.close("Fulfilled")
    result["dialogAction"]["message"] = {
        "contentType": "PlainText",
        "content": f"Here are some available task:\
                    \
                    {response_content}\
                    \
                    Choose one for today, copy the task id for later usage",
    }

    return result


@app.route(f"{ApiGroup.USER.value}/task/doing", methods=["POST"])
@utils.request_with_body
def get_my_task(data):
    user_id = data["userId"]
    current_intent = data["currentIntent"]

    stdout(data)

    response_content = ""
    list_doing_task = service.get_available_doing_task(user_id.split(":")[1], user_id)
    if len(list_doing_task) == 0:
        response_content = ""
    else:
        for item in list_doing_task:
            response_content += f'\n\n>*Task*:          {item["id"]}\
                                       >name:           {item["name"]}\
                                       >status:         {item["status"]}\
                                       >estimated:      {item["estimate"]}'

    result = dialogUtils.close("Fulfilled")

    if response_content == "":
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": "You have no pending task!. Please assign one",
        }
    else:
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f"Here are some doing task:\
                        \
                        {response_content}\
                        \
                        Copy the task id for later usage",
        }

    return result


@app.route(f"{ApiGroup.USER.value}/task/logwork", methods=["POST"])
@utils.request_with_body
def log_work(data):
    list_slot = ["TaskID", "LogHours", "LogContent"]
    user_id = data["userId"]
    current_intent = data["currentIntent"]
    slots = current_intent["slots"]
    slot_details = current_intent["slotDetails"]

    result = dialogUtils.delegate()

    stdout(data)
    stdout(slots)
    stdout(slot_details)

    # validate data

    if slot_details["TaskID"] and len(slot_details["TaskID"]["resolutions"]) > 0:
        slots["TaskID"] = slot_details["TaskID"]["resolutions"][0]["value"]

    if slot_details["LogHours"] and len(slot_details["LogHours"]["resolutions"]) > 0:
        slots["LogHours"] = slot_details["LogHours"]["resolutions"][0]["value"]

    exact_name = re.findall('"(.*?)"', data["inputTranscript"])

    if len(exact_name) > 0:
        slots["LogContent"] = exact_name[0]
    else:
        if (
            slot_details["LogContent"]
            and len(slot_details["LogContent"]["resolutions"]) > 0
        ):
            slots["LogContent"] = slot_details["LogContent"]["resolutions"][0]["value"]

    result["dialogAction"]["slots"] = slots

    # intent response

    if slots["TaskID"] and service.get_task_by_id(slots["TaskID"]) == None:
        result = dialogUtils.close("Failed")
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'Not found task with id {slots["TaskID"]}',
        }
        return result

    if current_intent["confirmationStatus"] == "None" and check_full_slots(
        list_slot, slots
    ):
        task = service.get_task_by_id(slots["TaskID"])
        result = dialogUtils.confirm_intent()
        result["dialogAction"]["intentName"] = current_intent["name"]
        result["dialogAction"]["slots"] = slots
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'Ok so your log will be:\
                        >*Task*:            {task.id}\
                        >log hours:         {slots["LogHours"]}\
                        >log content:       {slots["LogContent"]}\
                        \
                        Is this info correct ?',
        }
        return result

    # fulfillment
    if current_intent["confirmationStatus"] == "Confirmed":
        service.assign_work_log(slots["TaskID"], slots["LogContent"], slots["LogHours"])

    return result


@app.route(f"{ApiGroup.USER.value}/task/assign", methods=["POST"])
@utils.request_with_body
def assign_task(data):
    list_slot = [
        "TaskID",
        "TaskEstimate",
    ]
    user_id = data["userId"]
    current_intent = data["currentIntent"]
    slots = current_intent["slots"]
    slot_details = current_intent["slotDetails"]

    result = dialogUtils.delegate()

    stdout(data)
    stdout(slots)
    stdout(slot_details)

    # validate data

    if slot_details["TaskID"] and len(slot_details["TaskID"]["resolutions"]) > 0:
        stdout("log test")
        slots["TaskID"] = slot_details["TaskID"]["resolutions"][0]["value"]

    if (
        slot_details["TaskEstimate"]
        and len(slot_details["TaskEstimate"]["resolutions"]) > 0
    ):
        slots["TaskEstimate"] = slot_details["TaskEstimate"]["resolutions"][0]["value"]

    result["dialogAction"]["slots"] = slots

    # intent response

    if slots["TaskID"] and service.get_task_by_id(slots["TaskID"]) == None:
        result = dialogUtils.close("Failed")
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'Not found task with id {slots["TaskID"]}',
        }
        return result

    if current_intent["confirmationStatus"] == "None" and check_full_slots(
        list_slot, slots
    ):
        task = service.get_task_by_id(slots["TaskID"])
        result = dialogUtils.confirm_intent()
        result["dialogAction"]["intentName"] = current_intent["name"]
        result["dialogAction"]["slots"] = slots
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'\n\n>*Task*:           {task.id}\
                             >name:             {task.name}\
                             >status:           {task.status}\
                             >estimated:        {slots["TaskEstimate"]}\
                             \
                             Is this info correct ?',
        }
        return result

    # fulfillment
    if current_intent["confirmationStatus"] == "Confirmed":
        service.asign_task(user_id, slots["TaskID"], float(slots["TaskEstimate"]))

    return result


@app.route(f"{ApiGroup.USER.value}/task/markdone", methods=["POST"])
@utils.request_with_body
def markdone_task(data):
    list_slot = ["TaskID", "TaskStatus"]
    user_id = data["userId"]
    current_intent = data["currentIntent"]
    slots = current_intent["slots"]
    slot_details = current_intent["slotDetails"]

    result = dialogUtils.delegate()

    stdout(data)
    stdout(slots)
    stdout(slot_details)

    # validate data

    if slot_details["TaskID"] and len(slot_details["TaskID"]["resolutions"]) > 0:
        stdout("log test")
        slots["TaskID"] = slot_details["TaskID"]["resolutions"][0]["value"]

    if (
        slot_details["TaskStatus"]
        and len(slot_details["TaskStatus"]["resolutions"]) > 0
    ):
        slots["TaskStatus"] = slot_details["TaskStatus"]["resolutions"][0]["value"]

    result["dialogAction"]["slots"] = slots

    # intent response

    if slots["TaskID"] and service.get_task_by_id(slots["TaskID"]) == None:
        result = dialogUtils.close("Failed")
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'Not found task with id {slots["TaskID"]}',
        }
        return result

    if current_intent["confirmationStatus"] == "None" and check_full_slots(
        list_slot, slots
    ):
        task = service.get_task_by_id(slots["TaskID"])
        result = dialogUtils.confirm_intent()
        result["dialogAction"]["intentName"] = current_intent["name"]
        result["dialogAction"]["slots"] = slots
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'\n\n>*Task*:           {task.id}\
                              >name:            {task.name}\
                              >status:          {slots["TaskStatus"]}\
                              >estimated:       {task.estimated_hours}\
                              \
                              Is this info correct ?',
        }
        return result

    # fulfillment
    if current_intent["confirmationStatus"] == "Confirmed":
        service.markdone_task(slots["TaskID"], slots["TaskStatus"])

    return result


# def book_meeting_fulfill(data):
