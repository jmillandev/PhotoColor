from uuid import UUID

from src.color_palettes.entity import Colors
from src.color_palettes.finder import ColorPaletteFinder


async def find(photo_id: UUID) -> Colors:
    finder = ColorPaletteFinder()
    palette = await finder(photo_id)
    return palette.colors
