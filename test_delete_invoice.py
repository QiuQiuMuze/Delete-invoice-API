import requests
import json

url = "http://127.0.0.1:5000/deleteInvoice"
data = {"invoiceId": "456"}
data2 = {"invoiceId": "123"}
data3 = {"invoiceId": "789"}

response = requests.delete(url, json=data)
print("Status:", response.status_code)
print("Response:", response.json())

response = requests.delete(url, json=data2)
print("Status:", response.status_code)
print("Response:", response.json())

response = requests.delete(url, json=data3)
print("Status:", response.status_code)
print("Response:", response.json())
