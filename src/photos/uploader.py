from uuid import UUID

from fastapi import UploadFile
from kink import inject

from src.color_palettes.generator import ColorPaletteGenerator
from src.photo_stats.calculator import PhotoStatsCalculator
from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoUploader:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self, asset: UploadFile) -> Photo:
        photo = Photo.upload(filename=str(asset.filename), asset=asset.file.read())
        await photo.save()  # type: ignore[call-arg, misc]
        # TODO: Publish PhotoUploaded event
        # TODO: Remove UUID(str(..)) when the repository pattern is implemented
        await ColorPaletteGenerator()(photo.asset.file.read(), UUID(str(photo.id)))  # type: ignore[call-arg] # noqa: E501
        await PhotoStatsCalculator()(photo.asset.file.read(), UUID(str(photo.id)))  # type: ignore[call-arg] # noqa: E501
        return photo
