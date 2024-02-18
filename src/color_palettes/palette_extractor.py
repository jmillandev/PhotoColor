from .entity import Colors
from typing import Protocol, runtime_checkable

@runtime_checkable
class ColorPaletteExtractor(Protocol):
    async def __call__(self, asset: bytes) -> Colors:
        ...
