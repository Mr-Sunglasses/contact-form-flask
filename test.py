import requests

Base = "http://127.0.0.1:5000/"

response = requests.post(Base + "contact/kanishk/kanishk@fosscu.org")
print(response.json())