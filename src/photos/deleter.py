from uuid import UUID

from kink import inject

from src.photos.entity import Photo


@inject(use_factory=True)
class PhotoDeleter:
    # TODO: Inject PhotoRepository
    # TODO: Inject EventBus

    async def __call__(self, id: UUID) -> None:
        await Photo.delete(id)  # type: ignore[misc, arg-type]
        # TODO: Delete asset from storage - Use Domain Service
        # TODO: If Repositories were implemented, Publish PhotoDestroyed event
        # and listen it on color_palettes and stats modules
