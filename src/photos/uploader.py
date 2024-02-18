from uuid import UUID

from fastapi import UploadFile
from kink import inject

from src.color_palettes.generator import ColorPaletteGenerator
from src.photo_stats.calculator import PhotoStatsCalculator
from src.photos.entity import Photo
from .exceptions import CantUploadEmptyAsset, UnsupportedAssetMediaType

@inject(use_factory=True)
class PhotoUploader:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self, asset: UploadFile) -> Photo:
        asset_bytes = await asset.read()
        if not asset_bytes:
            # TODO: Raise this exception on PhotoAssetValueObject
            raise CantUploadEmptyAsset
        if not asset.content_type == "image/jpeg":
            # TODO: Raise this exception on PhotoAssetValueObject
            raise UnsupportedAssetMediaType

        photo = Photo.upload(filename=str(asset.filename), asset=asset_bytes)
        await photo.save()  # type: ignore[call-arg, misc]
        # TODO: Publish PhotoUploaded event
        # TODO: Remove UUID(str(..)) when the repository pattern is implemented
        await ColorPaletteGenerator()(asset_bytes, UUID(str(photo.id)))  # type: ignore[call-arg] # noqa: E501
        await PhotoStatsCalculator()(asset_bytes, UUID(str(photo.id)))  # type: ignore[call-arg] # noqa: E501
        return photo
