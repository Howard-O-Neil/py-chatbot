from marshmallow import Schema, fields

class SignUpDto(Schema):
  username = fields.Str()
  password = fields.Str()

