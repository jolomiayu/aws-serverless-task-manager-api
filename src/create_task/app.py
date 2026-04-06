import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    task = {
        'id': str(uuid.uuid4()),
        'title': body.get('title', '')
    }

    table.put_item(Item=task)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Task created',
            'task': task
        })
    }
