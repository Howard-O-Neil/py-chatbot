from pprint import pprint
from config import Config
from functools import reduce

from dateutil import parser
from application.share.dialog_utils import dialogUtils
from application.share.utils import utils, print_all, stdout
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from app import notification_group, lex_client
from .service import service
import requests
import json
import click
import re
import sched, time
import logging
import threading
import time

# s = sched.scheduler(time.time, time.sleep)
# def notify_logwork_all(sc): 
#     for team in service.get_all_project():

#         lex_response = lex_client.post_text(
#             botName=Config.AWS_LEX_BOT_NAME,
#             botAlias=Config.AWS_LEX_BOT_ALIAS,
#             userId=f'{Config.AWS_LEX_SLACK_CHANNEL}:{team.slack_team_id}:{team.slack_team_admin_id}',
#             inputText='notify logwork',
#         )
#         service.post_message_team_general(team.slack_team_id, lex_response["message"])
#     stdout(lex_response)

#     s.enter(3600, 1, notify_logwork_all, (sc,))

# s.enter(3600, 1, notify_logwork_all, (s,))
# s.run()


@notification_group.command("all")
def notify_logwork_all_cli(**kwargs):   
    for team in service.get_all_project():

        lex_response = lex_client.post_text(
            botName=Config.AWS_LEX_BOT_NAME,
            botAlias=Config.AWS_LEX_BOT_ALIAS,
            userId=f'cce65383-8176-4ce8-9642-c5848205cc18:{team.slack_team_id}:{team.slack_team_admin_id}',
            inputText='notify logwork',
        )
        service.post_message_team_general(team.slack_team_id, lex_response["message"])
    stdout(lex_response)
    pass

# post to general
