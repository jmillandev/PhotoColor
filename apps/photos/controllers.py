from uuid import UUID

from fastapi import UploadFile

from src.photos.uploader import PhotoUploader


async def upload(asset: UploadFile) -> UUID:
    uploader = PhotoUploader()
    photo = await uploader(asset)
    return photo.id
