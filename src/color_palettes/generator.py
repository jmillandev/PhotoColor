from uuid import UUID

from kink import inject

from .entity import ColorPalette
from .palette_extractor import ColorPaletteExtractor


@inject(use_factory=True)
class ColorPaletteGenerator:
    # TODO: Listen Event PhotoUploded
    # TODO: Inject ColorPaletteRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    def __init__(self, palette_extractor: ColorPaletteExtractor) -> None:
        self._extractor = palette_extractor

    async def __call__(self, asset: bytes, photo_id: UUID) -> ColorPalette:
        colors = await self._extractor(asset)
        palette = ColorPalette.generate(photo_id=photo_id, colors=colors)
        await palette.save()
        return palette
