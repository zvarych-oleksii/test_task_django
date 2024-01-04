import requests
from test_django_project.settings import API_KEY



def hunter_validator(email):
    api_key = API_KEY
    url = "https://api.hunter.io/v2/email-verifier"
    params = {"email": email, "api_key": api_key}
    response = requests.get(url, params=params)

    result_data = response.json().get("data", {})
    return result_data
