"""BL for email_validation."""

import requests

from test_django_project.settings import API_KEY


def hunter_validator(email):
    """Validate email against hunter."""
    api_key = API_KEY
    url = 'https://api.hunter.io/v2/email-verifier'
    email_model = {'email': email, 'api_key': api_key}
    response = requests.get(url, params=email_model, timeout=10)

    return response.json().get('data', {})
