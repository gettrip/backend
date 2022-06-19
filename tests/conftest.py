import pytest

from backend.app import create_app
from backend.models import create_all, drop_all
from backend.db import db_session, engine

from tests.factories import CityFactory, RouteFactory


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture
def testapp():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })

    app.connection = engine.connect()
    # create and fill database here
    create_all()

    yield app

    app.connection.close()
    # cleanup database here
    drop_all()



@pytest.fixture(scope="function")
def session(testapp):
    """
    Creates a new database session (with working transaction)
    for a test duration.
    """
    testapp.transaction = testapp.connection.begin()

    # pushing new Flask application context for multiple-thread
    # tests to work
    ctx = testapp.app_context()
    ctx.push()

    session = db_session()

    CityFactory._meta.sqlalchemy_session = session
    RouteFactory._meta.sqlalchemy_session = session

    yield session

    # the code after yield statement works as a teardown
    testapp.transaction.close()
    session.close()
    ctx.pop()


@pytest.fixture
def client(testapp):
    return testapp.test_client()


@pytest.fixture
def runner(testapp):
    return testapp.test_cli_runner()

