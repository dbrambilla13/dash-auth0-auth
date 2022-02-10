# Dash Auth0 OAuth

This is a simple library using Auth0 OAuth2.0 to authenticate and view a Dash app
written based on [dash-auth](https://github.com/plotly/dash-auth) and [dash-google-oauth](https://github.com/hossein-jazayeri/dash-google-oauth).
Upon authentication, a cookie is created and kept for 2 weeks.

### Setup
Setup an Auth0 tenant and application.

Add <your_app_base_url>/login/callback as allowed callback url and <your_app_base_url> as allowed logout url in the Auth0 Application settings.
For example:

    allowed callback url: https://www.myapp.com/login/callback
    allowed logout url:   https://www.myapp.com

Install the package:
```
$ pip install dash-auth0-oauth
```
Define following environment variables:
```
FLASK_SECRET_KEY

AUTH0_AUTH_URL
AUTH0_AUTH_SCOPE
AUTH0_AUTH_TOKEN_URI
AUTH0_AUTH_USER_INFO_URL
AUTH0_AUTH_CLIENT_ID
AUTH0_AUTH_CLIENT_SECRET
AUTH0_LOGOUT_URL
AUTH0_API_AUDIENCE
```
for example using [python-dotenv](https://pypi.org/project/python-dotenv/):
```
FLASK_SECRET_KEY="<some secret key>"

AUTH0_AUTH_URL="https://<your tenant url>/authorize"
AUTH0_AUTH_SCOPE="openid profile email"
AUTH0_AUTH_TOKEN_URI="https://<your tenant url>/oauth/token"
AUTH0_AUTH_USER_INFO_URL="https://<your tenant url>/userinfo"
AUTH0_AUTH_CLIENT_ID="<your app client id>"
AUTH0_AUTH_CLIENT_SECRET="<your app client secret>"
AUTH0_LOGOUT_URL="https://<your tenant url>/v2/logout"
AUTH0_API_AUDIENCE="<your_api_audience_identifier>"
```
Add it to the application:
```
app = Dash(__name__)

from dash_auth0_oauth.auth0_auth import Auth0Auth
auth = Auth0Auth(app)
```
You have access to `/logout` route in order to logout user by making a `GET` request.

User's name stored in cookie: `flask.request.cookies.get('AUTH-USER')`
