import boto3
import os
from pprint import pprint

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='eu-west-2')
tableName = os.environ['DYNAMODB_TABLE']

table = None

def getTable():
  pprint (tableName)
  if not tableName:
    raise ValueError("Table name not set up in environment")
  return dynamodb.Table(tableName)
