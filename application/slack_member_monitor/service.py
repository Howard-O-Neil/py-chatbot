from config import Config
from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from flask import jsonify
from entities.user import User
from .repository import repository

class Service:
    @utils.handle_service_error
    def handle_slack_member_event(self, data):
        return data

    @utils.handle_service_error
    def is_qualify_user(self, user_id):
        return repository.get_user_by_slack_id(user_id) != None
    
    @utils.handle_service_error
    def user_change_handle(self, data):
        slack_id = f'{Config.AWS_LEX_SLACK_CHANNEL}:{data["event"]["user"]["team_id"]}:{data["event"]["user"]["id"]}'
        user = repository.get_user_by_slack_id(slack_id)

        if user != None:
            if user.deleted_at == None:
                return repository.remove_user(slack_id)
            else: return repository.activate_user(slack_id)
        return ""
    
    @utils.handle_service_error
    def user_join_handle(self, data):
        user = User(
            slack_id = f'{Config.AWS_LEX_SLACK_CHANNEL}:{data["event"]["user"]["team_id"]}:{data["event"]["user"]["id"]}',
            name = data["event"]["user"]["profile"]["real_name_normalized"],
            phone = data["event"]["user"]["profile"]["phone"],
            email = data["event"]["user"]["profile"]["email"],
        )
        return repository.add_user(user, data["event"]["user"]["team_id"])


service = Service()