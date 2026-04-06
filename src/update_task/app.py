import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']
    body = json.loads(event['body'])

    title = body.get('title')

    table.update_item(
        Key={'id': task_id},
        UpdateExpression="set title = :t",
        ExpressionAttributeValues={
            ':t': title
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'Task updated successfully'
        })
    }
