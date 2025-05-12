Microservice A - Delete Invoice
Overview
This microservice allows the deletion of a specific invoice by its ID. It is designed to be used by another program through a REST API call. Each deletion attempt (success or failure) is logged in a JSON file for auditing purposes.

How to Request Data from This Microservice
HTTP Method:
DELETE

Endpoint:
http://127.0.0.1:5000/deleteInvoice
 Required Request Body (JSON):
{
  "invoiceId": "123"
}
Example Call in Python:
import requests

url = "http://127.0.0.1:5000/deleteInvoice"
payload = { "invoiceId": "123" }

response = requests.delete(url, json=payload)
print(response.json())
How to Receive Data from the Microservice
Response Format:
Content-Type: application/json

Example Response (success):
{
  "success": true,
  "message": "Invoice 123 deleted successfully."
}
Example Response (not found):
{
  "success": false,
  "message": "Invoice not found."
}
UML Sequence Diagram
Below is a simple UML sequence that describes how the request and response work between the test client and the microservice:


![UML Sequence Diagram](https://github.com/user-attachments/assets/114c4d4d-ea64-4b0c-9178-a4457f6fbb6b)


Log Format
All deletion attempts are saved in deletion_log.json in the following format:

{
  "timestamp": "2025-05-06T17:13:53.107724",
  "invoiceId": "789",
  "status": "not_found"
}
Repository Access
This microservice is available in the GitHub repo:
https://github.com/QiuQiuMuze/Delete-invoice-API

