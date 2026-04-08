import json
import logging
import boto3
import uuid
import jwt
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

SECRET_KEY = "mysecretkey"

def lambda_handler(event, context):
    try:
        logger.info(f"Incoming event: {json.dumps(event)}")

        # 🔐 AUTH CHECK
        headers = event.get("headers", {})
        auth_header = headers.get("Authorization") or headers.get("authorization")

        if not auth_header:
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "Missing token"})
            }

        token = auth_header.replace("Bearer ", "")

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception:
            return {
                "statusCode": 403,
                "body": json.dumps({"message": "Invalid token"})
            }

        # 💥 Error simulation
        if event.get("queryStringParameters") and event["queryStringParameters"].get("fail") == "true":
            raise Exception("Simulated failure for monitoring test")

        body = json.loads(event.get("body", "{}"))
        title = body.get("title", "No title")

        task_id = str(uuid.uuid4())
        item = {
            "id": task_id,
            "title": title
        }

        table.put_item(Item=item)

        logger.info(f"Task created: {item}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Task created (secured)",
                "task": item
            })
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
