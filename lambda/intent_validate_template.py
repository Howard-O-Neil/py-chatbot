# this is just a template, push this code on aws lambda to run

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
    

    url = get_parameters("PyChatbot-BE") + "/flower/order/validate"
    print(url)
    http = urllib3.PoolManager()
    response = http.request('POST', url,
                    body = json.dumps(event),
                    headers = {'Content-Type': 'application/json'},
                    retries = False)
    print(json.loads(response.data.decode("utf-8")))
    
    return json.loads(response.data.decode("utf-8"))