import os

from pydantic import BaseModel


class Server(BaseModel):
    port: str
    host: str
    token: str


class DataBase(BaseModel):
    url: str


class AppConfig(BaseModel):
    server: Server
    db: DataBase


def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    app_token = os.environ['APP_TOKEN']
    db_url = os.environ['DB_URL']
    return AppConfig(
        server=Server(port=app_port, host=app_host, token=app_token),
        db=DataBase(url=db_url),
    )


dev_config = load_from_env()

test_config = load_from_env()
test_config.db.url = os.environ['TEST_DB_URL']
