import requests
from requests.api import request

from .entities import Account


class AuthorizationException(Exception):
    pass


class ForbiddenException(Exception):
    pass


class MonzoClient:

    BASE_URL = 'https://api.monzo.com'

    def __init__(self, access_token):
        self._auth_header = {'authorization': 'Bearer {}'.format(access_token)}

    def _request(self, method, url):
        url = '{}{}'.format(self.BASE_URL, url)
        response = request(method, url, headers=self._auth_header)
        if response.status_code == 401:
            raise AuthorizationException(response.json()['message'])

        return response.json()

    @property
    def accounts(self):
        data = self._request('get', '/accounts')

        return [Account(d) for d in data['accounts']]
