from uuid import UUID

from kink import inject

from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoFinder:
    # TODO: Inject PhotoRepository

    async def __call__(self, id: UUID) -> Photo:
        return await Photo.find(id)
