from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from application.sign_up_account.dto.sign_up_dto import SignUpDto
from flask import jsonify
from entities.user import User
from .repository import repository

class Service:
    @utils.handle_service_error
    def sign_up(self, data: SignUpDto):
        raise NotFound('co con cac')
        new_user = User(**data)
        repository.add_data(new_user)
        stdout("=========== new user ===========")
        stdout(new_user)

service = Service()