# demo_social_auth
Facebook authentication implemented on Python/ Django using python-social-auth.

### Technologies:
Python==3.7.3

Django==2.2.1

postgres (PostgreSQL) 11.3

social-auth-app-django==3.1.0

## Features:
1. Implements Facebook authentication.

2. Supports extra data such as profile picture.

3. Supports [Long living access token](https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing/) - validity of 60 days.

## Setup:
Below variables are to be updated in `settings.py`

SOCIAL_AUTH_FACEBOOK_KEY : Facebook App ID

SOCIAL_AUTH_FACEBOOK_SECRET : Facebook App Secret

DB_NAME : Postgres Database Name

DB_USER : Postgres Database User

DB_PASSWORD : Postgres Database Password

DB_HOST : Postgres Database Host

DB_PORT : Postgres Database Port


## Notes:
For testing, use the same domain name as configured in the Facebook app.

If you have configured `localhost`, you might face issues, accessing `http://127.0.0.1:8000`. 

So, service should be accesible at `http://localhost:8000/`
