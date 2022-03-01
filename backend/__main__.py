import logging

from flask import Flask
from backend.cities import cities

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(cities, url_prefix='/api/v1/cities')


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')
    app.run(host='0.0.0.0', port=8080, debug=False)


if __name__ == "__main__":
    main()