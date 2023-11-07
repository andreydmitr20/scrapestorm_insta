import requests
from config import config

headers = {
    "accept": "application/json",
}

params = {
    "token": config.scrapestorm_api_key,
}

response = requests.get(
    "https://scrapestorm.net/api/token/status",
    params=params,
    headers=headers,
    timeout=config.scrapestorm_timeout_int,
)
print(response.text)

params = {"token": config.scrapestorm_api_key, "username": "metallica"}
print(params)
response = requests.get(
    config.scrapestorm_api_user_profile,
    params=params,
    headers=headers,
    timeout=config.scrapestorm_timeout_int,
)

print(response.text)
