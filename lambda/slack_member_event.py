import json
import urllib3

import boto3
ssm = boto3.client('ssm', 'ap-southeast-1')
def get_parameters(_name):
    response = ssm.get_parameters(
        Names=[_name],WithDecryption=True
    )
    for parameter in response['Parameters']:
        return parameter['Value']

def lambda_handler(event, context):
    url = get_parameters("PyChatbot-BE") + "/slack/member/event"
    print(url)

    event_body = json.loads(event["body"])
    event["body"] = event_body

    print(event)
    http = urllib3.PoolManager()
    response = http.request('POST', url,
                    body = json.dumps(event),
                    headers = {'Content-Type': 'application/json'},
                    retries = False)
    
    return event["body"]
