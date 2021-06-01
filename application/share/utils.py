from application.sign_up_account.dto.sign_up_dto import SignUpDto
import enum
import json
from functools import wraps
from pprint import pprint
from flask import request, Response
from marshmallow import ValidationError
from colored import fg, bg, attr
from uuid import uuid4
from werkzeug.exceptions import HTTPException

def print_all(object):
    pprint(vars(object))

def stdout(object):
    print(object, flush=True)

def log_err(err):
    stdout(f"========== {fg('red')}[ERROR]{attr('reset')} ==========")
    stdout(err)

def convert_to_json(object):
    return json.dumps(object.__dict__)

class AppResponseJson:
    def __init__(self, data, message):
        self.data = data
        self.message = message

class Utils:
    def validate(self, schema_class):
        def inner_function(func):
            wraps(func)
            def decorator(*args, **kwargs):
                result = None
                try:
                    result = schema_class().load(request.json)
                except ValidationError as err:
                    return Response(json.dumps(err.messages), 400, 
                        mimetype='application/json')

                return func(data=result, *args, **kwargs)
        
            decorator.__name__ = 'inner' + func.__name__
            return decorator

        inner_function.__name__ = uuid4().__str__()
        return inner_function

    def handle_service_error(self, func):
        wraps(func)
        def decorator(*args, **kwargs):
            result = None
            try:
                result = func(*args)
            except HTTPException as err:
                log_err(err)
                return Response(
                    convert_to_json(AppResponseJson(None, err.description)), err.code, 
                    mimetype='application/json')
            except Exception as err:
                stdout(f"========== {fg('red')}[ERROR]{attr('reset')} ==========")
                stdout(err)
                return Response(
                    convert_to_json(AppResponseJson(None, 'internal server error')), 500, 
                    mimetype='application/json')
            return result
        
        decorator.__name__ = func.__name__
        return decorator


utils = Utils()
# def rawImage(number):
#     for i in range(number):
#         url = "https://picsum.photos/1280/800"

#         response = requests.get(url, stream=True)
#         with open(f"static/{uuid.uuid4()}.png", "wb") as out_file:
#             shutil.copyfileobj(response.raw, out_file)

