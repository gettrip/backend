import logging

from backend.app import create_app
from backend.config import config

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')

    app = create_app()

    app.run(
        port=config.server.port,
        host=config.server.host,
        debug=False,
    )


if __name__ == '__main__':
    main()
