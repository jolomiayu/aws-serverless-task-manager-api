🚀 AWS Serverless Task Manager API

Deployed and tested on AWS with a live public API endpoint.

---

📌 Overview

This project demonstrates a fully serverless REST API built on AWS.

It allows users to:

- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks

The system is designed using an event-driven architecture and deployed using AWS SAM.

---

🏗️ Architecture

- AWS Lambda (compute)
- API Gateway (HTTP endpoints)
- DynamoDB (database)
- AWS SAM (deployment)
- AWS CodePipeline & CodeBuild (CI/CD)
- Amazon CloudWatch (monitoring)
- Amazon SNS (alerting)

---

⚙️ Tech Stack

- Python
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS SAM

---

🌐 Live API

https://2oev9ttl08.execute-api.eu-west-1.amazonaws.com/Prod

---

📡 API Endpoints

Method| Endpoint| Description
POST| /tasks| Create a task
GET| /tasks| Get all tasks
PUT| /tasks/{id}| Update a task
DELETE| /tasks/{id}| Delete a task
POST| /login| Authenticate user

---

🧪 Example Requests

🔐 Login (Get Token)

curl -X POST https://2oev9ttl08.execute-api.eu-west-1.amazonaws.com/Prod/login \
-H "Content-Type: application/json" \
-d '{"username":"admin","password":"password"}'

---

🚫 Request Without Token

curl -X POST https://2oev9ttl08.execute-api.eu-west-1.amazonaws.com/Prod/tasks \
-H "Content-Type: application/json" \
-d '{"title":"test"}'

---

✅ Request With Token

curl -X POST https://2oev9ttl08.execute-api.eu-west-1.amazonaws.com/Prod/tasks \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_TOKEN" \
-d '{"title":"secure task"}'

---

🚀 Deployment

sam build
sam deploy

---

🚨 Monitoring & Alerting (Project 9)

This project includes production-level monitoring and alerting:

- 📊 AWS CloudWatch Metrics for Lambda errors
- 🚨 CloudWatch Alarm triggered on failures
- 📩 SNS Email Notifications for real-time alerts

Test Monitoring

curl -X POST "https://2oev9ttl08.execute-api.eu-west-1.amazonaws.com/Prod/tasks?fail=true"

---

🔐 Authentication & Security (Project 10)

This project now includes JWT-based authentication to secure API endpoints.

Features

- 🔑 Login endpoint ("/login")
- 🔐 JWT token generation
- 🚫 Protected endpoints (require valid token)
- 🛡️ Unauthorized requests are blocked

How it works

1. User sends credentials to "/login"
2. Server returns a JWT token
3. Client includes token in request header:

Authorization: Bearer <token>

4. Lambda validates the token before processing the request

---

🎯 What I Learned

- Building serverless applications on AWS
- API Gateway + Lambda integration
- DynamoDB operations
- Infrastructure as Code using SAM
- CI/CD pipeline setup
- Monitoring and alerting systems
- Debugging real-world cloud issues
- Securing APIs with JWT authentication

---

💡 Future Improvements

- Use AWS Cognito for authentication
- Store secrets securely (AWS Secrets Manager)
- Add pagination
- Build a frontend (React)
- Implement role-based access control

---

👤 Author

Jolomi Ayu
