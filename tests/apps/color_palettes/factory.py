from src.color_palettes.entity import ColorPalette
from factory import LazyAttribute, Faker
from uuid import uuid4
from tests.factory import SQLAlchemyFactory
from random import randint

def generate_rgb():
    rgb = (f"{randint(0, 256):02x}" for _ in range(3))
    return '#' + ''.join(rgb)

class ColorPaletteFactory(SQLAlchemyFactory):
    class Meta:
        sqlalchemy_session = None
        model = ColorPalette

    id = LazyAttribute(lambda _: uuid4())
    photo_id = LazyAttribute(lambda _: uuid4())
    color1 = LazyAttribute(lambda _: generate_rgb())
    color2 = LazyAttribute(lambda _: generate_rgb())
    color3 = LazyAttribute(lambda _: generate_rgb())
    color4 = LazyAttribute(lambda _: generate_rgb())
    color5 = LazyAttribute(lambda _: generate_rgb())
