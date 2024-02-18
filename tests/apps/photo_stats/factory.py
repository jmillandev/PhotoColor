from src.photo_stats.entity import PhotoStat
from factory import LazyAttribute
from uuid import uuid4
from tests.factory import SQLAlchemyFactory
from random import randint

class PhotoStatFactory(SQLAlchemyFactory):
    class Meta:
        sqlalchemy_session = None
        model = PhotoStat

    id = LazyAttribute(lambda _: uuid4())
    photo_id = LazyAttribute(lambda _: uuid4())
    red = LazyAttribute(lambda _: randint(0, 100))
    green = LazyAttribute(lambda o: randint(0, 100 - o.red))
    blue = LazyAttribute(lambda o: 100 - o.red - o.green)
