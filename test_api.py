import requests
from config import config
headers = {
    'accept': 'application/json',
}

params = {
    'token': config.scrapestorm_api,
}

response = requests.get('https://scrapestorm.net/api/token/status',
                         params=params, headers=headers)

print(response.text)
