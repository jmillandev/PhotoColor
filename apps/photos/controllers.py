from uuid import UUID

from fastapi import UploadFile
from fastapi.responses import StreamingResponse

from src.photos.uploader import PhotoUploader
from src.photos.finder import PhotoFinder
from src.photos.deleter import PhotoDeleter
from io import BytesIO

async def upload(asset: UploadFile) -> UUID:
    uploader = PhotoUploader()
    photo = await uploader(asset)
    return photo.id

async def find(id: UUID) -> StreamingResponse:
    finder = PhotoFinder()
    photo = await finder(id)
    # TODO: photo.asset.file save on memory all file - Search for a way to stream the file
    return StreamingResponse(BytesIO(photo.asset.file.read()), media_type="image/jpeg")

async def delete(id: UUID) -> None:
    deleter = PhotoDeleter()
    await deleter(id)
