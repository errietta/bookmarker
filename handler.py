import json
from pprint import pprint

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def addUrl(event, context):
    pprint(event)

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
