from uuid import UUID

from kink import inject

from src.photos.entity import Photo
from src.shared.domain.exceptions.not_found import NotFound


@inject(use_factory=True)
class PhotoFinder:
    # TODO: Inject PhotoRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self, id: UUID) -> Photo:
        photo = await Photo.find(id)
        if not photo:
            raise NotFound("Photo not found")
        return photo
