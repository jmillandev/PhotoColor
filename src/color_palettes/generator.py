from uuid import UUID

from kink import inject

from .entity import ColorPalette, Colors


class ColorPaletteExtractor:
    async def __call__(self, asset: bytes) -> Colors:
        pass


@inject(use_factory=True)
class ColorPaletteGenerator:
    # TODO: Listen Event PhotoUploded
    # TODO: Inject ColorPaletteRepository

    async def __call__(self, asset: bytes, photo_id: UUID) -> ColorPalette:
        colors = await ColorPaletteExtractor()(asset)
        palette = await ColorPalette.generate(photo_id=photo_id, colors=colors)
        palette.save()
        return palette
