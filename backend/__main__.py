import logging

from backend.app import create_app
from backend.config import dev_config

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')

    app = create_app()

    app.run(
        port=dev_config.server.port,
        host=dev_config.server.host,
        debug=False,
    )


if __name__ == '__main__':
    main()
