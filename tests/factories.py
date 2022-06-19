import factory

from backend.models import City, Route


class CityFactory(factory.alchemy.SQLAlchemyModelFactory):

    uid = factory.Sequence(lambda n: '%s' % n)
    name = factory.Faker('city')
    image = factory.Faker('email')

    class Meta:
        model = City


class RouteFactory(factory.alchemy.SQLAlchemyModelFactory):

    uid = factory.Sequence(lambda n: '%s' % n)
    name = factory.Faker('city')
    city_id = 1
    image = factory.Faker('email')
    description = factory.Faker('text')
    duration = 100

    class Meta:
        model = Route
