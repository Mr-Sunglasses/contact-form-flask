import requests

Base = "http://127.0.0.1:5000/"

response = requests.post(Base + "contact/Anjuman Hassan/anjumanhassan@studentambasedor.com/I am Anjuman and I want to join fosscu.")
print(response.json())
print(response.status_code)