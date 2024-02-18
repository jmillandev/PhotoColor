from uuid import UUID

from kink import inject

from .entity import ColorPalette


@inject(use_factory=True)
class ColorPaletteFinder:
    # TODO: Inject ColorPaletteRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self, photo_id: UUID) -> ColorPalette:
        return await ColorPalette.find_by_photo_id(photo_id)
