from uuid import UUID

from kink import inject

from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoDeleter:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus

    async def __call__(self, id: UUID) -> Photo:
        return await Photo.delete(id)
        # TODO: If Repositories were implemented, Publish PhotoDestroyed event
        # and listen it on color_palettes and stats modules
