from fastapi import UploadFile
from kink import inject

from src.photos.entity import Photo
from src.color_palettes.generator import ColorPaletteGenerator
from src.photo_stats.calculator import PhotoStatsCalculator

@inject(use_factory=True)
class PhotoUploader:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus

    async def __call__(self, asset: UploadFile) -> Photo:
        photo = Photo.upload(filename=asset.filename, asset=asset.file.read())
        await photo.save()
        # TODO: Publish PhotoUploaded event
        await ColorPaletteGenerator()(photo.asset.file.read(), photo.id)
        await PhotoStatsCalculator()(photo.asset.file.read(), photo.id)
        return photo
