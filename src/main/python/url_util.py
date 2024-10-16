import requests

class UrlUtil:
    def __init__(self):
        pass

    def http_get(url, auth_token):
        headers = {
            "Authorization": auth_token
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()