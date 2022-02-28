import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Hello, world')    


if __name__ == "__main__":
    main()