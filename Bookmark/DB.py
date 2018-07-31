from DB import getTable
from pprint import pprint
import json

def createUser(args):
  pprint (args)

  table = getTable()
  table.put_item(
    Item={
      'UserName': args['userName'],
      'UserId': args['email']
    }
  )

def createBookmark(userId, args):
  pprint (args)

  table = getTable()
  response = table.update_item(
    Key={
      'UserId': userId,
    },
    UpdateExpression="set bookmarks = :bmarks",
    ExpressionAttributeValues={
      ':bmarks': [args]
    },
    ReturnValues="UPDATED_NEW"
  )

  print(json.dumps(response))