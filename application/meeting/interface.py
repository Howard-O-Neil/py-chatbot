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


@app.route(f"{ApiGroup.USER.value}/meeting/book", methods=["POST"])
@utils.request_with_body
def book_meeting(data):
    list_slot = [
        "MeetingStartTime",
        "MeetingName",
        "MeetingStartDate",
        "MeetingDuration",
        "MeetingLocation",
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
    if (
        slot_details["MeetingStartTime"]
        and len(slot_details["MeetingStartTime"]["resolutions"]) > 0
    ):
        meeting_start_time = slot_details["MeetingStartTime"]["resolutions"][0][
            "value"
        ].upper()

        time = parser.parse(meeting_start_time)
        time = time.replace(minute=(time.minute // 15) * 15)

        slots["MeetingStartTime"] = time.strftime("%I:%M %p")

    if (
        slot_details["MeetingDuration"]
        and len(slot_details["MeetingDuration"]["resolutions"]) > 0
    ):
        slots["MeetingDuration"] = slot_details["MeetingDuration"]["resolutions"][0][
            "value"
        ]

    exact_name = re.findall('"(.*?)"', data["inputTranscript"])

    if len(exact_name) > 1:
        slots["MeetingName"] = exact_name[0]
        slots["MeetingLocation"] = exact_name[1]
    elif len(exact_name) > 0:
        if slots["MeetingName"] == None:
            slots["MeetingName"] = exact_name[0]
        if slots["MeetingLocation"] == None:
            slots["MeetingLocation"] = exact_name[0]
    else:  # the very least option, not recommended to user
        if (
            slot_details["MeetingName"]
            and len(slot_details["MeetingName"]["resolutions"]) > 0
        ):
            slots["MeetingName"] = slot_details["MeetingName"]["resolutions"][0][
                "value"
            ]
        if (
            slot_details["MeetingLocation"]
            and len(slot_details["MeetingLocation"]["resolutions"]) > 0
        ):
            slots["MeetingLocation"] = slot_details["MeetingLocation"]["resolutions"][
                0
            ]["value"]

    if slots["MeetingLocation"] != None:
        find_location = service.get_location(slots["MeetingLocation"])
        if find_location == None:
            slots["MeetingLocation"] = None
        else:
            slots["MeetingLocation"] = find_location.name

    result["dialogAction"]["slots"] = slots

    # intent response

    if slots["MeetingStartDate"] and slots["MeetingStartTime"]:
        stdout("hula")
        if service.check_start_meeting(slots) != True:
            stdout("hula")
            result = dialogUtils.close("Failed")
            result["dialogAction"]["message"] = {
                "contentType": "PlainText",
                "content": "You cant have a meeting in the past",
            }
            return result

    if current_intent["confirmationStatus"] == "None" and check_full_slots(
        list_slot, slots
    ):
        result = dialogUtils.confirm_intent()
        result["dialogAction"]["intentName"] = current_intent["name"]
        result["dialogAction"]["slots"] = slots
        result["dialogAction"]["message"] = {
            "contentType": "PlainText",
            "content": f'Ok so your "{slots["MeetingName"]}"" will be on {slots["MeetingStartDate"]} at {slots["MeetingLocation"]}.\
                        Is this info correct ?',
        }
        return result

    # fulfillment
    if current_intent["confirmationStatus"] == "Confirmed":
        service.add_meeting(slots, user_id)

    return result


@app.route(f"{ApiGroup.USER.value}/meeting/location/available", methods=["POST"])
@utils.request_with_body
def available_meeting(data):
    current_intent = data["currentIntent"]

    response_content = ""
    for item in service.get_available_meeting_location(5):
        response_content += f'\n>{item["name"]}'

    result = dialogUtils.close("Fulfilled")
    result["dialogAction"]["message"] = {
        "contentType": "PlainText",
        "content": f"Here are some available location:\n\n {response_content}",
    }

    return result


# def book_meeting_fulfill(data):


@user_group.command("test")
def test(**kwargs):
    stdout(service.get_available_meeting_location(15))


@user_group.command("gen-meeting-location")
def gen_meeting_location(**kwargs):

    service.gen_location()
