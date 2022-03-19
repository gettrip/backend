import logging

from backend.app import create_app
from backend.config import load_from_env

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')

    app = create_app()
    app_config = load_from_env()

    app.run(
        port=app_config.server.port,
        host=app_config.server.host,
        debug=False,
    )


if __name__ == '__main__':
    main()
