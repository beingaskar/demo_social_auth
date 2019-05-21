from django.conf import settings

from social_django.models import UserSocialAuth

from auth_social.helper import FacebookGraphAPI


SOCIAL_AUTH_FACEBOOK_KEY = getattr(settings, 'SOCIAL_AUTH_FACEBOOK_KEY', None)
SOCIAL_AUTH_FACEBOOK_SECRET = getattr(settings, 'SOCIAL_AUTH_FACEBOOK_SECRET', None)


def set_long_live_access_token(backend, user, response, *args, **kwargs):
    """
    Replace the short term token with long lived token (validity of 60 days).
    https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing/

    :param backend: social_core.backends.facebook.FacebookOAuth2
    :param user: django.contrib.auth.models.User
    :param response: dict
    :return: None
    """

    if backend.name == 'facebook':
        if response['access_token']:
            response_long_lived_token = FacebookGraphAPI(
                SOCIAL_AUTH_FACEBOOK_KEY, SOCIAL_AUTH_FACEBOOK_SECRET
            ).get_long_lived_access_token(response['access_token'])

            if response_long_lived_token['status']:
                try:
                    social_auth = user.social_auth.get(provider="facebook")
                except UserSocialAuth.DoesNotExist:
                    social_auth = None
                except UserSocialAuth.MultipleObjectsReturned:
                    social_auth = None

                if social_auth:
                    social_auth.extra_data['access_token'] = response_long_lived_token['response']['access_token']
                    social_auth.extra_data['token_type'] = response_long_lived_token['response']['token_type']
                    social_auth.extra_data['expires'] = response_long_lived_token['response']['expires_in']
                    social_auth.save()
