from datetime import datetime
from social_core.exceptions import AuthForbidden
import requests

from authapp.models import User
from django.conf import settings


def save_user_email(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    access_token = response.get('access_token')
    email = dict(response)
    print(f'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa {email}')
    api_url = f'https://api.vk.com/method/users.get?fields=about,email&access_token={access_token}&v=5.131'
    response = requests.get(api_url)
    if response.status_code != 200:
        return
    data_json = response.json()['response'][0]
    print(data_json)
    if 'email' in data_json:
        user.email = data_json['email']
        print(data_json['email'])
