from email import message
import logging

from flask import Flask
from backend.cities import cities
from backend.user import user
from http import HTTPStatus
from werkzeug.exceptions import HTTPException
from backend.errors import AppError

logger = logging.getLogger(__name__)

def handle_http_exceptions(error: HTTPException):
    return {"message": error.description}, error.code

def handle_app_error(error: AppError):
    return {'message': error.reason}, error.status

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')

    app = Flask(__name__)

    app.register_blueprint(cities, url_prefix='/api/v1/cities') 
    app.register_blueprint(user, url_prefix='/api/v1/users')

    app.register_error_handler(HTTPException, handle_http_exceptions)
    app.register_error_handler(AppError, handle_app_error)

    app.run(host='0.0.0.0', port=8080, debug=False)


if __name__ == "__main__":
    main()