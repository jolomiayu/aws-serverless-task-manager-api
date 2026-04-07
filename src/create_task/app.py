import json
import logging
import boto3
import uuid

# Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    try:
        # ✅ Log incoming request
        logger.info(f"Incoming event: {json.dumps(event)}")

        # ✅ Simulate failure (for testing alarms later)
        if event.get("queryStringParameters") and event["queryStringParameters"].get("fail") == "true":
            raise Exception("Simulated failure for monitoring test")

        # Parse body
        body = json.loads(event.get("body", "{}"))
        title = body.get("title", "No title")

        # Create item
        task_id = str(uuid.uuid4())
        item = {
            "id": task_id,
            "title": title
        }

        # Save to DynamoDB
        table.put_item(Item=item)

        # ✅ Log success
        logger.info(f"Task created: {item}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task created via CI/CD",
                "task": item
            })
        }

    except Exception as e:
        # ✅ Log error
        logger.error(f"Error occurred: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
