from fastapi import UploadFile
from kink import inject

from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoUploader:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus

    async def __call__(self, asset: UploadFile) -> Photo:
        photo = Photo.upload(filename=asset.filename, asset=asset.file.read())
        await photo.save()
        # TODO: Publish PhotoUploaded event
        return photo
