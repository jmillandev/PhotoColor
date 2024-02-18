from uuid import uuid4

from factory import LazyAttribute  # type: ignore[import-untyped]

from src.photos.entity import Photo
from tests.factory import SQLAlchemyFactory


class PhotoFactory(SQLAlchemyFactory):
    class Meta:
        model = Photo
        sqlalchemy_session = None

    id = LazyAttribute(lambda _: uuid4())
    asset = LazyAttribute(
        lambda _: open("tests/fixtures/images/sample.jpg", "rb").read()
    )
