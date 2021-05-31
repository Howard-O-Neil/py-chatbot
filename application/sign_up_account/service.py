from application.sign_up_account.dto.sign_up_dto import SignUpDto
from flask import jsonify
from entities.user import User
from .repository import repository

class Service:
    def sign_up(self, data: SignUpDto):
        print(data)

        res = repository.add_data(User(**data))

service = Service()