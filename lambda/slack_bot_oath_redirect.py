import json
import urllib3
import os

import boto3

ssm = boto3.client("ssm", "ap-southeast-1")


def get_parameters(_name):
    response = ssm.get_parameters(Names=[_name], WithDecryption=True)
    for parameter in response["Parameters"]:
        return parameter["Value"]


def revoke_token(http, _token):
    revoke_uri = "https://slack.com/api/auth.revoke"
    revoke_res = http.request("POST", revoke_uri, fields={"token": _token})
    print(json.loads(revoke_res.data.decode("utf-8")))
    return json.loads(revoke_res.data.decode("utf-8"))


def request_token(http, event):
    code = event["queryStringParameters"]["code"]
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    client_token = os.environ["CLIENT_TOKEN"]

    redirect_uri = os.environ["REDIRECT_URI"]
    uri = f"https://slack.com/api/oauth.v2.access?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}"
    response = http.request("GET", uri)

    print(json.loads(response.data.decode("utf-8")))
    return json.loads(response.data.decode("utf-8"))


def check_is_signed_team(http, prefix, team_id):
    check_uri = f"{prefix}/project/validate/is-signed?team_id={team_id}"
    check_response = http.request("GET", check_uri)
    check_res = json.loads(check_response.data.decode("utf-8"))

    print(check_res)
    return check_res


def sign_up_token(http, prefix, request_token_res):
    sign_up_token_response = http.request(
        "POST",
        f"{prefix}/project/token/bot/sign-up",
        body=json.dumps(request_token_res),
        headers={"Content-Type": "application/json"},
        retries=False,
    )
    sign_up_token_res = json.loads(sign_up_token_response.data.decode("utf-8"))

    print(sign_up_token_res)
    return sign_up_token_res


def get_all_user_info(http, token, team_id):
    get_response = http.request(
        "POST",
        "https://slack.com/api/users.list",
        fields={
            "token": token,
            "team_id": team_id,
        },
    )

    get_res = json.loads(get_response.data.decode("utf-8"))
    print(get_res)
    return get_res


def lambda_handler(event, context):
    http = urllib3.PoolManager()

    request_token_res = request_token(http, event)

    # some checking system
    team_id = request_token_res["team"]["id"]
    prefix = get_parameters("PyChatbot-BE")

    check_res = check_is_signed_team(http, prefix, team_id)

    if check_res["status"] == "failed":
        revoke_token(http, request_token_res["access_token"])
        return {"message": check_res["message"]}

    sign_up_token_res = sign_up_token(http, prefix, request_token_res)

    if sign_up_token_res["status"] == "failed":
        revoke_token(http, request_token_res["access_token"])

        return {"message": check_res["message"]}
    else:
        return {
            "message": "install app sucessful",
            "url": f"https://app.slack.com/client/{team_id}",
        }

    return handler_result
