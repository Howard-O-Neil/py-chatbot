from datetime import date, datetime, timedelta
import math
from entities.meeting import Meeting
from entities.meeting_location import MeetingLocation
from application.share.dialog_utils import DialogUtils, dialogUtils
from werkzeug.exceptions import NotFound
from application.share.utils import print_all, stdout, utils
from entities.user import User
from .repository import repository
from uuid import uuid4
from entities.project import Project
from dateutil import parser
import click
import json


class Service:
    @utils.handle_service_error
    def gen_location(self):
        data = [
            "Kickstart Meetings",
            "Leaders Think Space",
            "Banding Together",
            "The Capital City",
            "Fellowship Hall",
            "Gathering Place",
            "Gig Gallery",
            "The Steam Room",
            "Chromatic Commons",
            "Collective IQ Room",
            "Community Spot",
            "Convening Space",
            "First World Problems",
            "Flatiron Room",
            "Gathering Field",
        ]

        for name in data:
            meeting_location = MeetingLocation(id=uuid4(), name=name)
            repository.add_data(meeting_location)
        pass

    # def parse_aws_duration(self, data):

    def is_qualify_user(self, user_id):
        return repository.get_user_by_slack_id(user_id) != None
        

    def is_empty_intent(self, list_slot, slots):
        for slot_type in list_slot:
            if slots[slot_type] != None:
                return False
        return True

    def get_location(self, location_name):
        return repository.find_meeting_location_by_name(location_name)

    def check_start_meeting(self, slots):
        start_meeting = parser.parse(slots["MeetingStartDate"])
        start_time = parser.parse(slots["MeetingStartTime"])

        start_meeting = start_meeting.replace(hour=start_time.hour)
        start_meeting = start_meeting.replace(minute=start_time.minute)

        if start_meeting <= datetime.now():
            return False
        return True

    def add_meeting(self, slots, user_id):
        start_meeting = parser.parse(slots["MeetingStartDate"])
        start_time = parser.parse(slots["MeetingStartTime"])

        start_meeting = start_meeting.replace(hour=start_time.hour)
        start_meeting = start_meeting.replace(minute=start_time.minute) 

        end_meeting = start_meeting + timedelta(hours=int(slots["MeetingDuration"]))

        meeting = Meeting(
            name=slots["MeetingName"],
            start=start_meeting,
            end=end_meeting,
            assignee=repository.get_user_by_slack_id(user_id).id,
            location_id=self.get_location(slots["MeetingLocation"]).id
        )
        return repository.add_meeting(meeting)

    def get_available_meeting_location(self, limit_res):
        res = [
            { "name": item.name }
            for item in repository.get_available_meeting_location(limit_res)
        ]
        stdout("=======================")
        for name in res:
            stdout(name['name'])
        stdout("=======================")

        return res


service = Service()
