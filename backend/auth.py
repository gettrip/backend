from flask_httpauth import HTTPTokenAuth

from backend.config import dev_config

auth = HTTPTokenAuth(scheme='Bearer')

app_token = dev_config.server.token

tokens = {app_token: 'verified'}


@auth.verify_token
def verify_token(token):
    return tokens.get(token)
