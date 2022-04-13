import os

from pydantic import BaseModel


class Server(BaseModel):
    port: str
    host: str


class DataBase(BaseModel):
    url: str
    token: str


class AppConfig(BaseModel):
    server: Server
    db: DataBase


def load_from_env() -> AppConfig:
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    db_url = os.environ['DB_URL']
    db_token = os.environ['APP_TOKEN']
    return AppConfig(
        server=Server(port=app_port, host=app_host),
        db=DataBase(url=db_url, token=db_token),
    )


config = load_from_env()
