import json
import jwt
import datetime

SECRET_KEY = "mysecretkey"

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    username = body.get("username")
    password = body.get("password")

    if username == "admin" and password == "password":
        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")

        return {
            "statusCode": 200,
            "body": json.dumps({"token": token})
        }

    return {
        "statusCode": 401,
        "body": json.dumps({"message": "Invalid credentials"})
    }
