from typing import Protocol, runtime_checkable

from .entity import Colors


@runtime_checkable
class ColorPaletteExtractor(Protocol):
    async def __call__(self, asset: bytes) -> Colors:
        ...
