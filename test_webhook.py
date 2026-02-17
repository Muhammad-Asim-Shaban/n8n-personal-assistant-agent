import requests 


user_message= "Hi how are you?"

request_message={
    "message":user_message
}

url = "http://localhost:5678/webhook-test/22cc08b6-4807-454d-b979-0cbc2304a339"

response=requests.post(url=url, json=request_message)

print(response.status_code)