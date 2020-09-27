import requests
import json


def server_response(link) -> str:
    response = requests.get(link)
    json_data = json.loads(response.text)
    return json_data
