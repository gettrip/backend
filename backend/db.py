from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


def get_db(url: str) -> scoped_session:
    engine = create_engine(url)
    return scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
