import factory

from backend.models import City


class CityFactory(factory.alchemy.SQLAlchemyModelFactory):

    uid = factory.Sequence(lambda n: '%s' % n)
    name = factory.Faker('name')
    image = factory.Faker('email')

    class Meta:
        model = City
