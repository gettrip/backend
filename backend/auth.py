from flask_httpauth import HTTPTokenAuth

from backend.config import config

auth = HTTPTokenAuth(scheme='Bearer')

db_token = config.db.token

tokens = {db_token: 'verified'}


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens.get(token)
