from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from flask import jsonify
from entities.user import User
from .repository import repository

class Service:
    @utils.handle_service_error
    def sign_up(self, data):
        team_id = data["team_id"]
        user = User(
            slack_id = data['slack_id'],
            name = data["name"],
            phone = data["phone"],
            email = data["email"],
        )
        return repository.add_user(user, team_id)
        

service = Service()