import requests


API_ROOT = 'https://graph.facebook.com/'
DEFAULT_TIMEOUT = 30


class FacebookGraphAPI(object):
    """
    Facebook Graph API Helper Class.
    """

    def __init__(self, app_id, secret_key, **kwargs):
        """
        :param app_id: string
        :param secret_key: string
        """

        self.app_id = app_id
        self.secret_key = secret_key
        self.timeout = kwargs.pop('timeout', DEFAULT_TIMEOUT)

    def __get_headers(self):
        """
        Returns required HTTP headers for the API request to Facebook.

        :return: dict
        """

        return {}

    def connect_to_remote(self, url, params):
        """
        Hits the Facebook Graph API with given parameters and returns response.

        :param url: URL
        :param params: dict
        :return: dict
        """

        response = requests.get(
            url, params, headers=self.__get_headers(), timeout=self.timeout
        )

        response_data = response.json()

        return {
            'status': True if response.status_code == 200 else False,
            'response': response_data
        }

    def get_long_lived_access_token(self, short_lived_token):
        """
        Returns the long lived access token (valid for 60 days) corresponding
        to given `short_lived_token`

        :param short_lived_token: string
        """

        assert isinstance(short_lived_token, str)

        end_point = "oauth/access_token"

        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.app_id,
            'client_secret': self.secret_key,
            'fb_exchange_token': short_lived_token
        }

        url = API_ROOT + end_point

        return self.connect_to_remote(url, params)
