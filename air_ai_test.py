import requests
from time import sleep

url = "https://chat.air.ai/api/v1/calls"

while(True):
    payload = {
        "promptId": 29919,
        "phone": "+12086501288",
        "name": "Jorge",
        "metadata": {}
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdJZCI6Im9yZ18yVVhyY2g0U2ZHU2FUQUFEa2R4ZDdTdFVZRHQiLCJpYXQiOjE2OTk2MzMwMTF9.sr2eq1iJB4WqBs-55lXJWVIdpN-omlGkm-9KkKZR7_Y"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

    sleep(5)

