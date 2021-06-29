from application.share.dialog_utils import dialogUtils
import click
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import app
from .service import service
import copy
import json


@app.route(f"{ApiGroup.FLOWER.value}/order/validate", methods=["POST"])
@utils.request_with_body
def order_flower_validate(data):
    list_required_slot = ["FlowerType", "PickupTime", "PickupDate"]

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
        slot_details["FlowerType"]
        and len(slot_details["FlowerType"]["resolutions"]) > 0
    ):
        slots["FlowerType"] = slot_details["FlowerType"]["resolutions"][0]["value"]

    if (
        slot_details["PickupTime"]
        and len(slot_details["PickupTime"]["resolutions"]) > 0
    ):
        slots["PickupTime"] = slot_details["PickupTime"]["resolutions"][0][
            "value"
        ].upper()
        slots["PickupTime"].replace("PM", "evening")
        slots["PickupTime"].replace("AM", "morning")


    result["dialogAction"]["slots"] = slots

    # invoke fulfill code
    if current_intent["confirmationStatus"]:
        if current_intent["confirmationStatus"] == "Confirmed":
            order_res = order_flower(data)
            # result["dialogAction"]["message"] = {
            #     "contentType": "PlainText",
            #     "content": "See you again",
            # }
    return result


# fulfillment code
def order_flower(data):
    # stdout(data)
    service_res = service.order_flower(data)

    # if fail -> return dialogAction close on failed

    return dialogUtils.delegate()
