from dash import Dash
from dash import html

app = Dash(__name__)

from dash_auth0_oauth.Auth0_auth import Auth0Auth
auth = Auth0Auth(app)


app.layout = html.Div(
    [
        html.H1('Hello World'),
        html.A(html.Button('click to logout'), href='/logout')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)