from application.sign_up_account.dto.sign_up_dto import SignUpDto
import shutil
from functools import wraps
from pprint import pprint
from typing import Any, Callable, Generic, Type, TypeVar
from flask import request, Response
from marshmallow import ValidationError
import uuid
import json

def print_all(object):
    pprint(vars(object))


class Utils:
    def validate(self, schema_class):
        def inner_function(func):
            wraps(func)
            def decorator(*args, **kwargs):
                result = None
                try:
                    result = schema_class().load(request.json)
                except ValidationError as err:
                    print_all(err)
                    return Response(json.dumps(err.messages), 400, 
                        mimetype='application/json')

                return func(data=result, **kwargs)
        
            decorator.__name__ = 'inner' + func.__name__
            return decorator
        return inner_function

utils = Utils()
# def rawImage(number):
#     for i in range(number):
#         url = "https://picsum.photos/1280/800"

#         response = requests.get(url, stream=True)
#         with open(f"static/{uuid.uuid4()}.png", "wb") as out_file:
#             shutil.copyfileobj(response.raw, out_file)

