from uuid import UUID

from kink import inject

from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoFinder:
    # TODO: Inject PhotoRepository
    # TODO: Add Unit Test Case using Mocks(After implementing the repository pattern)

    async def __call__(self, id: UUID) -> Photo:
        return await Photo.find(id)
