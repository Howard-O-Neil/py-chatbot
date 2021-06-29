from application.share.dialog_utils import DialogUtils, dialogUtils
from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from entities.user import User
from .repository import repository

import json

class Service:
    @utils.handle_service_error
    def order_flower(self, data):
        return
        

service = Service()