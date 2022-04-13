from flask_httpauth import HTTPTokenAuth

from backend.config import load_from_env

auth = HTTPTokenAuth(scheme='Bearer')

db_config = load_from_env()
db_token = db_config.db.token

tokens = {db_token: 'verified'}


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens.get(token)
