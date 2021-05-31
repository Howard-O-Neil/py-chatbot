from marshmallow import Schema, fields
from marshmallow_dataclass import dataclass

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import NumberParseException, number_type

def check_phone(phone):
    try: phonenumbers.parse(phone)
    except NumberParseException:
        return False
    return carrier._is_mobile(number_type(phonenumbers.parse(phone)))

class SignUpDto(Schema):
    facebook_url = fields.Url(required=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True, validate=check_phone)
    email = fields.Email(required=True)
