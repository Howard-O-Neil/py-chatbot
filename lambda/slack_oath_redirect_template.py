import json
import urllib3
import os

import boto3

ssm = boto3.client("ssm", "ap-southeast-1")


def get_parameters(_name):
    response = ssm.get_parameters(Names=[_name], WithDecryption=True)
    for parameter in response["Parameters"]:
        return parameter["Value"]


def lambda_handler(event, context):
    http = urllib3.PoolManager()

    print(context)
    print(event)
    
    code = event["queryStringParameters"]["code"]
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    redirect_uri = os.environ['REDIRECT_URI']
    uri = f"https://slack.com/api/oauth.v2.access?code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}"
    response = http.request("GET", uri)
    res = json.loads(response.data.decode("utf-8"))
    
    # some checking system
    admin_id = res["authed_user"]["id"]
    team_id = res["team"]["id"]
    prefix = get_parameters("PyChatbot-BE")
    check_uri = f"{prefix}/project/validate/is-signed?admin_id={admin_id}&team_id={team_id}"
    check_response = http.request("GET", check_uri)
    check_res = json.loads(check_response.data.decode("utf-8"))
    
    print(json.loads(response.data.decode("utf-8")))
    print(check_res)
    
    handler_result = {}
    
    if check_res["status"] == "failed":
        revoke_uri = "https://slack.com/api/auth.revoke"
        revoke_res = http.request('POST', revoke_uri,
                        fields={
                            "token": res["access_token"]
                        })

        print(json.loads(revoke_res.data.decode("utf-8")))

        handler_result = {
            "message": check_res["message"]
        }
    else:
        handler_result = {
            "message": "install app sucessful",
            "url": f"https://app.slack.com/client/{team_id}"
        }

    return handler_result