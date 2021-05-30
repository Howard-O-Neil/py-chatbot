from entities.user import User
from application.share.security import secure
from application.share.api_constraint import ApiGroup
from flask import jsonify, request
from app import app, db

@app.route(f'{ApiGroup.USER.value}/sign-up', methods=['POST'])
@secure.user_auth
def sign_up():
  # print(request.json)
  account = User(facebook_url="123", name="tmk", phone="0938147189", email="12345")
  return request.json

@app.route(f'{ApiGroup.USER.value}/get-data1', methods=['GET'])
@secure.user_auth
def get_data1():
  return 'get_data1'