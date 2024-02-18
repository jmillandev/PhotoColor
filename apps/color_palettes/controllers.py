from typing import Tuple
from uuid import UUID

from src.color_palettes.finder import ColorPaletteFinder


async def find(photo_id: UUID) -> Tuple[str, str, str, str, str]:
    finder = ColorPaletteFinder()
    palette = await finder(photo_id)
    return palette.colors
